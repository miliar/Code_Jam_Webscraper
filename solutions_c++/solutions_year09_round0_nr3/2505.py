#include <iostream>
#include <cassert>
#define MAX_LINE 512

char welcome_msg[] = "welcome to code jam";

unsigned long long solve(char *line_ptr, int line_size, char *msg_ptr)
{
   assert (line_size >= 0);

   if (*msg_ptr == '\0')
      return 1;

   unsigned long long total = 0;

   for (int i(0); i<line_size; i++) {
      if (line_ptr[i] == *msg_ptr) {
         total += solve(line_ptr + i+1, line_size - i-1, msg_ptr+1);
      }
   }

   return total;
}

int main(int argc, char **argv)
{
   int N;
   std::cin >> N;
   std::cin.get(); // read \n

   for (int i(0); i<N; i++) {
      char line[MAX_LINE];
      std::cin.getline(line, MAX_LINE);
      unsigned long long result = solve(line, strlen(line), welcome_msg);
      printf("Case #%d: %04llu\n", i+1, result);
   }
   return 0;
}
