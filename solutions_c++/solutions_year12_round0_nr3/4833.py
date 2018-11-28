#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <fstream>
#include <istream>

using namespace std;

int isrecycled(int,int);
void rotate(char*,int,int);
void swap(char*,int,int);

int main(void)
{
	ifstream infile;
        infile.open("input.txt");
	string cases;
	getline(infile,cases);
	int count = atoi(cases.c_str());

	for(int i=0;i<count;i++)
	{
		string line;
		getline(infile,line);
		
		char *dup = strdup(line.c_str());
		char *token = strtok(dup, " ");
		int low = atoi(token);
		token = strtok(NULL, " ,.-");
		int high = atoi(token);

		//cout<<"low:"<<low<<"high:"<<high<<endl;

		int count = 0;
		for(int j=low;j<high;j++)
		{
			for(int k=j+1;k<=high;k++)
			{
				//if(j==k) continue;
				int result = 0;
				result = isrecycled(j,k);
				if(result == 1) 
				{
					//cout<<j<<" "<<k<<endl;
					count += 1;
				}
			}
		}
		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
}

int isrecycled(int input1,int input2)
{
	char temp1[100];
	char temp2[100];

	sprintf(temp1, "%i", input1);
	sprintf(temp2, "%i", input2);

	int temp1_len = strlen(temp1);

	int rotations = temp1_len-1;
	int rotations_count = 1;
	while(rotations_count<=rotations)
	{
		rotate(temp1,strlen(temp1),1);
		rotations_count++;
		if(strcmp(temp1,temp2)==0)
		{
			//cout<<"i was here"<<endl;
			return 1;
		}
	}
	return 0;
}

void rotate(char* input,int n,int r)
{
        int i,j;
        r = r % n;
        while(r>0)
        {
                for(i=0;i<n-1;i++)
                {
                        swap(input,i,i+1);

                }

                r--;
        }
}

void swap(char *input,int index1,int index2)
{
        int temp = input[index1];
        input[index1] = input[index2];
        input[index2] = temp;
}
