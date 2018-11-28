#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "iostream"
using namespace std;


struct list_store{
			int index;
			int case_count;
		  };


class list_obj{ public:
		int first_index, last_index, list_count;
		char id;
		list_store *list;
		

			list_obj(char a)
			{id=a;
			 list_count=0;}

			void fill_list(char *str)
			{
			 list=new list_store[last_index-first_index+1];
			 for(int i=first_index;i<=last_index;i++)
			  if(str[i]==id)
				{list[list_count].index=i;
				 list_count++;}
			}

			int find_first_index(char *str, int starting_index)
			{int i;
			 for(i=starting_index; i<strlen(str); i++)
				if(str[i]==id)
				{first_index=i;
				 break;}
			 return i;
			}


			int find_last_index(char *str, int finishing_index)
			{int i;
			 for(i=finishing_index; i>=0; i--)
				if(str[i]==id)
				{last_index=i;
				 break;}
			 return i;
			}
	      };
			 
main()
{
	int no_test_case;
	scanf("%d",&no_test_case);
	for(int i=-1;i<no_test_case;i++)
	{
		 bool continue_flag=false;
		 int number_of_cases=0;
		 char welcome_string[510];
		 cin.getline(welcome_string,510);
if(i==-1)continue;
		 char sequence[]="welcome to code jam";
		 list_obj *obj_array[19];

		 for(int j=0;j<19;j++)
		 obj_array[j]=new list_obj(sequence[j]);
		 
		 int begin_index=0,finish_index=strlen(welcome_string);

		 for(int j=0;j<19;j++)
			{int new_begin_index=obj_array[j]->find_first_index(welcome_string,begin_index);
			 begin_index=new_begin_index;
			 	if(begin_index==strlen(welcome_string))
			 	{continue_flag=true;break;}
			}
		 if(continue_flag==true)
			{printf("Case #%d: %04d\n", i+1, number_of_cases);
			 continue;}


		 for(int j=18;j>=0;j--)
			{int new_finish_index=obj_array[j]->find_last_index(welcome_string,finish_index);
			 finish_index=new_finish_index;
				if(finish_index<0)
				{continue_flag=true;break;}
			}
		 if(continue_flag==true)
			{printf("Case #%d: %04d\n", i+1, number_of_cases);
			 continue;}


		 for(int j=0;j<19;j++)
			obj_array[j]->fill_list(welcome_string);

		 	for(int j=0;j<obj_array[18]->list_count;j++)
				obj_array[18]->list[j].case_count=1;

		for(int j=17;j>=0;j--)
		{for(int k=0;k<obj_array[j]->list_count;k++)
			{
			 obj_array[j]->list[k].case_count=0;
					for(int l=0;l<obj_array[j+1]->list_count;l++)
						if(obj_array[j]->list[k].index<obj_array[j+1]->list[l].index)
		 					obj_array[j]->list[k].case_count=(obj_array[j]->list[k].case_count+obj_array[j+1]->list[l].case_count)%10000;
			}
		}

		for(int j=0;j<obj_array[0]->list_count;j++)
		number_of_cases+=obj_array[0]->list[j].case_count;

		printf("Case #%d: %04d\n", i+1, number_of_cases%10000);

	}

return 0;
}











