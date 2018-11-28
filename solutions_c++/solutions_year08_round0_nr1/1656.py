#include <stdio.h>
#include <string>
#include <vector>

using std::string;
using std::vector;


void main ()
{
  FILE* input_file;
  char filename[1024];
  string output = "";
  
  printf("Type the name of the input file: ");
  gets(filename);
  input_file = fopen(filename, "rt");
  while(!input_file)
  {
   printf("There's been a problem opening the input file. Type the name of the file again: ");
   gets(filename);
   input_file = fopen(filename, "rt");
  }


  int case_num, search_num, query_num;
  char tmp[128];
  
  fscanf(input_file, "%d\n", &case_num);
  
  for(int c = 0; c < case_num; c++)
  {
    // file reading
    vector<string> search_engs, queries;
    
    fscanf(input_file, "%d\n", &search_num);
    fflush(stdin);
    for(int s = 0; s < search_num; s++)
    {
      fgets(tmp, 127, input_file);
      search_engs.push_back(tmp);
    }
    
    fscanf(input_file, "%d\n", &query_num);
    fflush(stdin);
    for(int q = 0; q < query_num; q++)
    {
     fgets(tmp, 127, input_file);
     queries.push_back(tmp);
    }

    // data processing
    vector<string> search_list = search_engs;
    vector<string>::iterator it, list_it;
    string chosen;
    int switches = 0;

    for(it = queries.begin(); it != queries.end(); it++)
    {
     if(search_list.size() == 1)
      chosen = *search_list.begin();
     for(list_it = search_list.begin(); list_it != search_list.end(); list_it++)
     {
      if(*it == *list_it)
      {
       search_list.erase(list_it);
       break;
      }
     }
     if(search_list.size() == 0)
     {
      switches++;
      search_list = search_engs;
      for(list_it = search_list.begin(); list_it != search_list.end(); list_it++)
      {
       if(*list_it == chosen)
       {
        search_list.erase(list_it);
        break;
       }
      }
     }
    }

    // output
    sprintf(tmp, "Case #%d: %d\n", c+1, switches);
    output += tmp;
  }

  FILE* output_file;

  output_file = fopen("output.txt", "wt");
  printf(output.c_str());
  if(!output_file)
  {
   printf("There's been a problem creating the output file. The program will be finished without writing the output.");
   exit(0);
  }
  fprintf(output_file, "%s", output.c_str());

  fclose(output_file);
  fclose(input_file);
}
