char ciph[26];
#include <stdio.h>
#include<iostream>
using namespace std;
void makeciph()
{
	char in_test[]={"ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvqz"};
	char out_test[]={"ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupzq"};

	for(int i=0,j;i<26;++i)
	{
		j=0;
		while(in_test[j]!=char(i+97))
			++j;
		ciph[i]=out_test[j];
	}
}

int main() {
	makeciph();
	char in_t[101],temp;//out_t[101]
	int num_t,i;
	scanf("%d",&num_t);
	getchar(); ///scanf leaves \0 in buffer, apparently
	for(int j=1;j<=num_t;++j)
	{
		cin.getline(in_t,101,'\n');
		//scanf("%[^'\n']s",in_t);
		printf("Case #%d: ",j);
		for(i=0;*(in_t+i)!='\0';++i)
		{
			temp=*(in_t+i);
			if(temp!=' ' )
			{
				printf("%c", *( ciph+ (int(temp)-97) ) );
			}
			else
				printf(" ");
		}
		printf("\n");
	}
	return 0;
}
