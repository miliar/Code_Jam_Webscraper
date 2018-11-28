// author:  molendaj@gmail.com

#include <stdlib.h>
#include <stdio.h>
#include <conio.h>
#include <stdarg.h>
#include <string.h>


/*******************************************************************************
 *
 ******************************************************************************/

typedef unsigned char uint8_t;
typedef unsigned short uint16_t;
typedef unsigned int uint32_t;


typedef signed char int8_t;
typedef signed short int16_t;
typedef signed int int32_t;


/*******************************************************************************
 *
 ******************************************************************************/

#define LOG_FILE_NAME                        "log.txt"


/*******************************************************************************
 * globals
 ******************************************************************************/

FILE* log_file;

/*******************************************************************************
 *
 ******************************************************************************/

void dual_printf(char *fmt, ...);
int main(int argc, char * argv[]);
int real_main(int argc, char * argv[]);


/*******************************************************************************
 * prints to a file and to Std Out
 ******************************************************************************/
void dual_printf(char *fmt, ...)
{
   va_list ap;

   // do printf
   va_start(ap, fmt);
   vprintf(fmt, ap);  // write to stdout
   va_end(ap);

   // do file output
   va_start(ap, fmt);
   vfprintf(log_file, fmt, ap);  // write to log file
   va_end(ap);

   fflush(log_file);
}


/*******************************************************************************
 *
 ******************************************************************************/
int main(int argc, char * argv[])
{
   log_file = fopen(LOG_FILE_NAME, "wt");
   printf("Saving results to '%s'...\n", LOG_FILE_NAME);

   if (log_file == NULL)
   {
      printf("error: opening file '%s'\n", LOG_FILE_NAME);
      return 0;
   }


   real_main(argc, argv);


   fclose(log_file);


   printf("Done!\n");
   printf("Press any key to continue . . . ");
   getch();


   return 0;
}


/*******************************************************************************
 *
 ******************************************************************************/
int real_main(int argc, char * argv[])
{
   FILE* input_file;

   input_file = fopen("input.txt", "rt");
   if (input_file == NULL)
   {
      return 0;
   }

   uint32_t num_test_cases;
   fscanf(input_file, "%d\n", &num_test_cases);

   for (uint32_t test_case_num = 0; test_case_num < num_test_cases; test_case_num++)
   {
      uint32_t Nbr_googlers;
      uint32_t Surprising_nbr;
      uint32_t P_at_least;
      uint32_t persons_score[100];

      fscanf(input_file, "%d %d %d", &Nbr_googlers, &Surprising_nbr, &P_at_least);
      //dual_printf("%d %d %d", Nbr_googlers, Surprising_nbr, P_at_least);

      for (uint32_t current_person = 0; current_person < Nbr_googlers; current_person++)
      {
         fscanf(input_file, "%d", &persons_score[current_person]);
         //dual_printf(" %d", persons_score[current_person]);
      }
      //dual_printf("\n");

      uint32_t max_google_who_could= 0;
      uint32_t nbr_surprises_given = 0;
      for (uint32_t current_person = 0; current_person < Nbr_googlers; current_person++)
      {
         uint32_t one_persons_sum;
         one_persons_sum = persons_score[current_person];

         uint32_t one_persons_max_without_surprise;
         one_persons_max_without_surprise = (one_persons_sum + 2) / 3;

         if (one_persons_max_without_surprise >= P_at_least)
         {
            max_google_who_could++;
         }
         else if (one_persons_sum >= 2)
         {
            if ((one_persons_max_without_surprise + 1) == P_at_least)
            {
               if (nbr_surprises_given < Surprising_nbr)
               {
                  if ((one_persons_sum % 3) == 1)
                  {
                     // no advantage to a surprise
                  }
                  else
                  {
                     max_google_who_could++;
                     nbr_surprises_given++;
                  }
               }
            }
         }
      }

      //fscanf(input_file, "\n");

      dual_printf("Case #%d: %d", test_case_num + 1, max_google_who_could);
      dual_printf("\n");
   }


   fclose(input_file);
   return 0;
}


/*******************************************************************************
 * END OF FILE
 ******************************************************************************/


