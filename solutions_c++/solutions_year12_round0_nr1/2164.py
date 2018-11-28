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
   char alphabet[26];
   char found[26];

   memset(&found, 0, sizeof(found));

   alphabet['z' - 'a'] = 'q';
   alphabet['q' - 'a'] = 'z';

   char string1[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
   char string2[] = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

   for (uint32_t xx = 0; xx < strlen(string1); xx++)
   {
      if (string1[xx] != ' ')
      {
         char one_char;
         one_char = char (string1[xx] - 'a');
         found[one_char] = 1;
         alphabet[one_char] = string2[xx];
      }
   }

   for (uint32_t xx = 0; xx < sizeof(alphabet); xx++)
   {
      //printf("%c -> %c\n", xx + 'a', alphabet[xx], found[xx]);
   }

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
      char some_string[110];

      fscanf(input_file, "%[^\n]\n", &some_string[0]);
      //dual_printf("'%s'\n", some_string);

      dual_printf("Case #%d: ", test_case_num + 1);
      for (uint32_t xx = 0; xx < strlen(some_string); xx++)
      {
         if (some_string[xx] != ' ')
         {
            dual_printf("%c", alphabet[some_string[xx] - 'a']);
         }
         else
         {
            dual_printf(" ");
         }
      }
      dual_printf("\n");
   }


   fclose(input_file);
   return 0;
}


/*******************************************************************************
 * END OF FILE
 ******************************************************************************/


