// p1.cpp : Defines the entry point for the console application.
//


#pragma warning(disable: 4786)
#include "stdafx.h"
#include<stdlib.h>
#include<stdio.h>
#include<ctype.h>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <functional>
#include <sstream>
#include <hash_map>
#include <unordered_map>

 
using namespace std ;

int _tmain(int argc, _TCHAR* argv[])
{
	int A,B,T,count=0;
	int cross[10000],permCount,perm[6000];

	FILE * pFile;
	FILE * pOut;
	string strNum;
	char *chr;

	
	pFile = fopen ("C:\\Output\\p3s.in","r");
	pOut = fopen ("C:\\Output\\p3sOut.out","w");

	if (pFile == NULL) perror ("Error opening file");
   else {


	//( fgets (mystring , 100 , pFile) != NULL )
	fscanf(pFile, "%d",&T);

	
	int rCount=0;

	for(int i=0;i<T;i++){

		fscanf(pFile, "%d",&A);
		fscanf(pFile, "%d",&B);
		

		fprintf(pOut,"Case #%d: ",i+1);

		
		rCount=0;
		for(int j=0;j<10000;j++)
		{
			cross[j]=0;
		}
		
		unordered_map <string, int> hmap;


		for(int k=A;k<=B;k++)
		{

			//if(cross[k]==1)continue;

			 std::ostringstream oss1;

			oss1<< k;

  
			strNum= oss1.str();

			int len=strNum.length();


			/*std::sort(strNum.begin(), strNum.end());*/
			permCount=0;

			/*do {
        
			char *aa=new char[strNum.size()+1];
			aa[strNum.size()]=0;
			memcpy(aa,strNum.c_str(),strNum.size()); 

			int n1=atoi(aa);
			perm[permCount++]=n1;


			} while(std::next_permutation(strNum.begin(), strNum.end()));*/
			char chArr[100];
			
			itoa(k,chArr,10);
			perm[permCount++]=atoi(chArr);
			for(int p=0;p<len-1; p++)
			{
				char ch;
				
				ch=chArr[0];
				int q;

				for(q=0;q<len-1;q++)
				{
					
					chArr[q]=chArr[q+1];
				}
				chArr[q]=ch;

				perm[permCount++]=atoi(chArr);
			}

			 

			for(int m=0;m<permCount;m++)
			{
				if(perm[m]>=A&&perm[m]<=B)
				{
					char  s11[50],s12[50],s13[50];

						itoa(k,s12,10);
						strcpy( s11,s12);
						itoa(perm[m],s12,10);
						strcat(s11,",");
						strcat(s11,s12);

						if(hmap[s11]==1)
						{
							continue;
						}

					if(k<perm[m])
					{
						
						rCount++;

						char  s1[50],s2[50],s3[50];

						itoa(k,s2,10);
						strcpy( s1,s2);
						itoa(perm[m],s2,10);
						strcat(s1,",");
						strcat(s1,s2);

						hmap[s1]=1;

						itoa(perm[m],s2,10);
						strcpy( s1,s2);
						itoa(k,s2,10);
						strcat(s1,",");
						strcat(s1,s2);

						hmap[s1]=1;

						//cross[k]=1;
						//cross[perm[m]]=1;
					}
				}

			}

		}
	

		




		fprintf(pOut,"%d\n",rCount);
      
    
   }

	
	 fclose (pFile);
	 fclose (pOut);
	}
	return 0;
}



