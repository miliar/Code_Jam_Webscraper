#include <stdio.h>
#include <algorithm>
#include <vector>

using std::string;
using std::vector;

bool compare(int i, int j)
{
 return i>j;
}

int main ()
{
 FILE* input_file, *output_file;
 char filename[128];

 printf("Type the name of the input file: ");
 gets(filename);
 input_file = fopen(filename, "rt");
 if(!input_file)
  printf("There's been a problem opening the input file.");
 output_file = fopen("output.txt", "wt");


 int case_num, coord_num, tmp;

 fscanf(input_file, "%d", &case_num);

 for(int c = 0; c < case_num; c++)
 {
  vector<int> a_coords, b_coords;

  // file reading    
  fscanf(input_file, "%d", &coord_num);
  for(int s = 0; s < coord_num; s++)
  {
   fscanf(input_file, "%d ", &tmp);
   a_coords.push_back(tmp);
  }
  for(int s = 0; s < coord_num; s++)
  {
   fscanf(input_file, "%d ", &tmp);
   b_coords.push_back(tmp);
  }
  sort(a_coords.begin(), a_coords.end());
  sort(b_coords.begin(), b_coords.end(), compare);

  int scalar_prod = 0;
  for(int i = 0; i < coord_num; i++)
  {
   scalar_prod += a_coords[i]*b_coords[i];
  }

  fprintf(output_file, "Case #%d: %d\n", c+1, scalar_prod);
 }

 return 1;
}