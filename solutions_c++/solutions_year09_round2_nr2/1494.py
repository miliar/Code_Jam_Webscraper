#include <iostream>
#include <fstream>
#include <cstring>
#include <vector>
#include <stdlib.h>
using namespace std;

//string original;
char * original = new char [25];
char * minn = new char [25];
char * lowest = new char [25];
bool flag = false;
bool found = false;

int swap(char* first, char* second)
{
        char ch = *second;
        *second = *first;
        *first = ch;
}

int permute(char* set, int begin, int end)
{
        int i;
        int range = end - begin;
       
        if (range == 1)
	{		
		//cout<<"xxx "<<set<<" "<<original<<" "<<strcmp(original, set)<<endl;
		if(set[0] != '0')
		{
			if(strcmp(lowest, set) >= 0)
			{
				strcpy(lowest, set);
			}
		}
		//cout<<lowest<<endl;
		
		if(strcmp(original, set) < 0)
		{
			
			found = true;
			if(flag == false)
			{
				strcpy(minn, set);
				flag = true;
			}
			//cout<<set<<" "<<minn<<" "<<strcmp(set,minn)<<endl;
			if(strcmp(set, minn) <= 0)
			{
				
				strcpy(minn, set);
				
			}
		}
		
			
			
        } 
	else 
	{
	        for(i = 0; i < range; i++) 
		{
                        swap(&set[begin], &set[begin + i]);		//initial swap
                        permute(set, begin + 1, end);				//recursion
                        swap(&set[begin], &set[begin + i]);       //swap back
                }
        }
        return 0;
}

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("B-small-attempt1.in");
	fout.open("B-small.out");
	
	int T;	
		
	fin >> T;
	
	for(int i = 0; i < T; i++)
	{
		string s;
		fin >> s;
		char * str = new char[25];
		strcpy(str, s.data());
		strcpy(original, str);
		strcpy(lowest, original);
		//strcpy(minn, original);
		found = false;
		flag = false;
		
		permute(str, 0, s.length());
		
		if(!found)
		{
/*			cout<<"ok";
			s.push_back('0');
			strcpy(str, s.data());
			//strcpy(original, str);
			//strcpy(minn, original);
			found = false;
			flag = false;
			permute(str, 0, s.length());
			
			{
				fout<< minn << endl;
			}
*/
		
			s = lowest;
			//cout<<s;
			s.insert(1, 1, '0');
			fout<<"Case #"<<i+1<<": "<<s<<endl;
		}
		else
		{
			fout<<"Case #"<<i+1<<": "<<minn<<endl;
		}
		
	}
		
		
	
	
}
