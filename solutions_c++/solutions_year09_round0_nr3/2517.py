/* Google Code Jam 2009
   Qualification Round

   Problem: C

   author: David Volgyes
   address: david.volgyes@gmail.com


 */

#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <iostream>
#include <fstream>

char* sourceText="welcome to code jam";

long process(char* src,const char* target)
{long result=0;

for(int i=0;i<strlen(target);++i)
{
	if (target[i]==src[0])
	{
		//std::cout<<src[0]<<" == " << target[i] << std::endl;
		if (src[1]!=0)
			result+=process(src+1,target+i);
		else
			result+=1;
	}
}
return result%10000;
}

int main() {
	int testCases;
	int i=0;
	long result=0;
	std::string text;
	std::cin>>testCases;
	getline(std::cin,text);
	do{
		++i;
		getline(std::cin,text);
		result=process(sourceText,text.c_str());
		printf("Case #%i: %04li\n",i,result);


	}
	while(i<testCases);

	return 0;
}
