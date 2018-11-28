#include <stdio.h>
#include <iostream>
int main(){
	int alphabet[26];
	int i,j,k;
	char *in = "A-small-attempt1.in";
	char *out ="result.out";
	char ch;
	freopen(in,"rt",stdin);
	freopen(out,"wt",stdout);
	int numberofTestCases;
	int no = 1;
	bool isNew=true;
	char example[] = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup";
	char decrypt[] = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv";
	for(i=0;1;++i){
		if(example[i] == '\0')
			break;
		alphabet[(int)decrypt[i]-97]=example[i];
	}
	alphabet['z'-97]='q';
	alphabet['q'-97]='z';
	scanf("%d",&numberofTestCases);
	getchar();
	while(1){
		if(scanf("%c",&ch) == EOF)
			break;
		if(isNew){
			std::cout<<"Case #"<<no<<": ";
			isNew = false;
		}
		if(ch>96 && ch<123){
			std::cout<<(char)alphabet[ch-97];
			//printf("%c",alphabet[ch-97]);
		}
		else{
			std::cout<<ch;
			//printf("%d",ch);
		}
		if(ch=='\n'){
			++no;
			isNew = true;
		}
	}

	return 0;
}
