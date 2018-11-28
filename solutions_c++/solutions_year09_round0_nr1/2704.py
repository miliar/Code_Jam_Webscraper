#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include<conio.h>
#include<string.h>
using namespace std;

int search(char a,string str)
{
       int i;
       for(i=0;str[i]!=NULL;i++)
       {
              if(str[i]==a)
                 return 1;
       }
       return 0;
}


int main()
{
	ifstream fin ("a.in");
	ofstream fout ("a.out");
	int L,D,N, tmp;
	string tempWord1,tempWord2;
	int m,l;
    string s1;
    int flag ;
	string compstr;
	int i,len,j,count;
	fin >> L;
	fin >> D;
	fin >> N;
    vector<string> words;
    vector<string> acceptedWords;
 	vector<string> dictionary;
    dictionary.erase(dictionary.begin(), dictionary.end());	
    for (i=0;i<D;i++)
    {
        fin>>tempWord1;
	    dictionary.push_back(tempWord1); 
         
    }
    
       
    //loop for number of test cases
    for(i=0;i<N;i++)
    {
          words.erase(words.begin(), words.end());	
          tempWord1="";
    
          fin>>tempWord1;
          for(j=0;tempWord1[j]!=NULL;j++)
          {
               tempWord2="";
               if(tempWord1[j]=='(')
               {
                     j++;
                     while(tempWord1[j]!=')')
                     {
                         tempWord2 = tempWord2 + tempWord1[j];
                         j++;
                     }
               }
               else
               {
                     tempWord2 = tempWord1[j];                       
               }
               words.push_back(tempWord2);
         }
         
         //loop through dictionary
         count = 0;
         for(m=0;m<D;m++)
         {
              s1 = dictionary[m];
              //loop through each element of the word in dictionary
              flag=1;
              for(l=0;s1[l]!=NULL;l++)
              {
                   flag=search(s1[l],words[l]);
                   //compstr = words[l];
                   
                   if(flag==0)
                      break;
              }
              if(flag==1)
                         count++;
         }
         fout << "Case #" <<  i+1 << ": " << count << endl;
         
}
return 0;
}


       
