#include<iostream>
#include<fstream>
#include<string.h>
#include "Trie.hpp"
using namespace std;
void GetCount(int** level, int i,  struct Node* n, int L, Trie* t);
int Getid(char id);
void ClearLevels(int** levels, int L);

int totalcount = 0;

int main()
{
   ifstream ipfile1;
   int L=0;
   int D=0;
   int N=0;
   string s;
   ipfile1.open("input.txt");
   Trie* t;
   int** level;
   int flag = 0;
   int levelid = -1;
   int id;
   char* testcase;
   t = new Trie();

   if (ipfile1.is_open())
   {
	ipfile1>>L;
	ipfile1>>D;
	ipfile1>>N;
	level = (int**)malloc(sizeof(int*)*L);
	for (int i=0; i<L; i++)
	{
		level[i] = (int*)malloc(sizeof(int)*26);
		
	}
	
	getline(ipfile1, s);

	for (int i=0; i<D; i++)
	{
		getline(ipfile1, s);
		t->InsertString(s.c_str());
	}
	
	for (int i=0; i<N; i++)
	{
		ClearLevels(level, L);
		getline(ipfile1, s);
		testcase = (char*)malloc(sizeof(char)*(s.length()+1));
		bzero(testcase, s.length()+1);
		strcpy(testcase, s.c_str());
		flag = 0;
		levelid = -1;

                for (int j=0; j<s.length(); j++)
                {
                        if (testcase[j] == '(')
                        {
                                flag = 1;
				levelid++;
                        }
                        else if (testcase[j] == ')')
                        {
                                flag = 0;
                                continue;
                        }
                        else
                        {
                                if (flag == 0)
                                {
					levelid++;
                                }
				id = Getid(testcase[j]);
				level[levelid][id] = 1;
                        }

		
		}


		GetCount(level, 0, t->root, L, t);
		cout<<"Case #"<<(i+1)<<": "<<totalcount<<endl;
		totalcount = 0;
	}
    }

}




void ClearLevels(int** levels, int L)
{
  for (int i=0; i<L; i++)
  {
	for (int j=0; j<26; j++)
	{
		levels[i][j] = 0;
	}
  }
return;
}

int Getid(char id)
{
 return((int)id-97);
}


void GetCount(int** level, int i,  struct Node* n, int L, Trie* t)
{
  struct Node* temp;
  int flag= 0;
    for (int j=0; j<26; j++)
    {
	if (level[i][j] == 1)
	{
		temp = t->CheckTrieNode(j, n, &flag);
		if ( flag == 1 && i == L-1)
		{
			totalcount++;
		}
		else if (temp !=NULL)
		{
			i = i+1;
			GetCount(level, i, temp, L, t);
			i= i-1;
		}
	}
	
    }
}
