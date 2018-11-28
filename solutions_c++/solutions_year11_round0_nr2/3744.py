//visual studio express
// Magicka.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <hash_map>
#include <string>
#include <deque>

using namespace std;

void readTestCase(hash_map<string , char>&  InvokeMap, hash_map<char , char>&  OppositeMap, int frequency[])
{
	InvokeMap.clear();
	OppositeMap.clear();

	for (int i=0;i<=40; ++i)
		frequency[i] = 0;

	int C=0, D=0;

	string temp;
	char readWord[15];

	scanf("%[ \n]", readWord);
	scanf("%i", &C);
	scanf("%[ \n]", readWord);

	for (int i=1; i<=C;++i)
	{
		scanf("%[A-Z]", readWord);
		temp = "";
		temp += readWord[0];
		temp += readWord[1];
		InvokeMap[temp] = readWord[2];

		temp = "";
		temp += readWord[1];
		temp += readWord[0];
		InvokeMap[temp] = readWord[2];
	}

	scanf("%i", &D);
	scanf("%[ \n]", readWord);
	for (int i=1; i<=D; ++i)
	{
		scanf("%[A-Z]", readWord);
		OppositeMap[readWord[0]] = readWord[1];
		OppositeMap[readWord[1]] = readWord[0];
	};
}

void processMove(deque<char>& queue, hash_map<string,char>&  InvokeMap,
				  hash_map<char , char>&  OppositeMap,int frequency[40])
{
	bool proceed = true;
	string temp = "";

	while (proceed)
	{
		proceed = false;
		hash_map<string,char>::iterator it;
		hash_map<char,char>::iterator itTwo;

		string invokeWord = "";
		if (queue.size() >=2)
		{
			invokeWord += queue[queue.size()-1];
			invokeWord += queue[queue.size()-2];
		}
		
		//transformacja
		if (queue.size()>=2 && (it = InvokeMap.find(invokeWord)) != InvokeMap.end() )
		{
			char newVal = InvokeMap[invokeWord];
			{
				proceed = true;
				frequency[queue.back() -'A'] -=1;
				queue.pop_back();
				frequency[queue.back() -'A'] -=1;
				queue.pop_back();
				queue.push_back(newVal);
				frequency[queue.back() -'A'] +=1;
				proceed = true;
			}
		};

		//usuwanie
		if (queue.size() >=2 && (itTwo = OppositeMap.find(queue.back())) != OppositeMap.end())
		{
			if ( frequency [ OppositeMap[queue.back()] - 'A'] >=1){
				for (int i=0; i<=40 ; ++i)
					frequency[i] = 0;
				queue.clear();
			};
		}


	}

}

int main(int argc, char* argv[])
{
	 freopen ("c://temp//B-small-attempt0.in","r",stdin);
	 freopen ("c://temp//magicka.out","w",stdout);

	 int T,N;
	 hash_map<string, char>  InvokeMap;
	 hash_map<char, char>  OppositeMap;
	 int frequency[44];
	 char temp[10];

	 scanf("%i", &T);

	 for (int i=1; i<= T; ++i)
	 {
		 readTestCase(InvokeMap, OppositeMap, frequency);
		 scanf("%i", &N);
		 deque<char> queue;
		 char curr;

		 scanf("%[ \n]", temp);
		 for (int j=1; j<=N;++j)
		 {
			 scanf("%c", &curr);
			 queue.push_back(curr);
			 frequency[ curr - 'A'] +=1;
			 processMove(queue, InvokeMap, OppositeMap, frequency);
		 };

		 printf("Case #%i: [", i);
		 for (int k=0;k<queue.size(); ++k)
		 {
			 if (k!=0)
				 printf(", %c", queue[k]);
			 else
				 printf("%c", queue[k]);

		 };
		 printf("]\n");
	 };


	 
	 fclose (stdout);
	 fclose (stdin);

	return 0;
}

