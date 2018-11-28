// author:  molendaj@gmail.com

#include <stdlib.h>
#include <stdio.h>
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
   return 0;
}


/*******************************************************************************
 *
 ******************************************************************************/
int real_main(int argc, char * argv[])
{
   FILE* input_file = fopen("input.txt", "rt");
   if (input_file == NULL)
   {
      return 0;
   }

   uint32_t num_test_cases;
   fscanf(input_file, "%d\n", &num_test_cases);
   for (uint32_t test_case_num = 0; test_case_num < num_test_cases; test_case_num++)
   {
      uint32_t AA;
      uint32_t BB;
      fscanf(input_file, "%d %d", &AA, &BB);
      //dual_printf("%d %d\n", AA, BB);

      // 2000000
      // 1234567
      char nn_as_string[8];
      char new_string[8];

      //fscanf(input_file, "\n");
      uint32_t solution = 0;

      for (uint32_t nn = AA; nn < BB; nn++)
      {
         itoa(nn, nn_as_string, 10);
         uint32_t nn_string_len = strlen(nn_as_string);


         int32_t mms_found[8];
         uint32_t num_mms_found = 0;
         for (uint32_t gg = 0; gg < 8; gg++)
         {
            mms_found[gg] = -1;
         }

         uint32_t mm;
         for (uint32_t zz = 0; zz < nn_string_len; zz++) // try nn all combinations
         {
            uint32_t yy;
            for (yy = 0; yy < nn_string_len; yy++)
            {
               new_string[yy] = nn_as_string[(zz + yy) % nn_string_len];
            }
            new_string[yy] = NULL;

            {
               mm = atoi(new_string);
               uint32_t mm_string_len = strlen(new_string);

               // if starts if 0's, bad
               if (nn_string_len != mm_string_len)
               {
                  // bad
                  continue;
               }

               if (mm > BB)
               {
                  // bad
                  continue;
               }
               if (nn < mm)
               {
                  // good
               }
               else
               {
                  // bad
                  continue;
               }
            }

            // found a rotation of nn that match mm
            // check if we already found the nn,mm pair
            for (uint32_t gg = 0; gg < 8; gg++)
            {
               if ((uint32_t)mms_found[gg] == mm)
               {
                  goto next;
               }
            }
            mms_found[num_mms_found] = mm;
            num_mms_found++;

            solution++;
            //dual_printf("nn:  %d, mm:  %d, [zz] -> %d\n", nn, mm, zz);

            next:
         } // try nn all combinations seeing if match mm
      } // nn loop


      dual_printf("Case #%d: %d\n", test_case_num + 1, solution);
   }


   fclose(input_file);


   return 0;
}


/*******************************************************************************
 * END OF FILE
 ******************************************************************************/


