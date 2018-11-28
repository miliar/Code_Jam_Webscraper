#include <stdio.h>
#include <stdlib.h>
#include <string>
using std::string;

string test;
string etalon;
int searchnext(int &num, char tc){
	if(num==-1) return num;
	while(num<test.length() && test[num]!=tc) num++;
	if(!(num<test.length())) return num=-1;
	return ++num;
}

int main(){
	int N;
	etalon="welcome to code jam";
	int iEtalon=0;
	int mas[19]; //"welcome to code jam"
	int count=0;
	char buf[1000];
	scanf("%d\n",&N);
	for(int i=0;i<N;i++){
		count=0;
		gets(buf);
		test=buf;
		//first doing
		if(test.length()>=etalon.length()){
			int j=0; //start position for search
			for(int iet=0;iet<etalon.length();iet++)
				mas[iet]=searchnext(j,etalon[iet]);
			if(mas[18]!=-1){
				int j9=18;
				while(j9>=0){
					while(mas[j9]!=-1)
					{
						j=mas[j9];
						mas[j9]=searchnext(j,etalon[j9]);
						if(j9==18){
							count++;
							if(count>=10000) count-=10000;
						}else if(mas[j9]!=-1){
							j=mas[j9];
							for(int j8=j9+1;j8<19;j8++)
								mas[j8]=searchnext(j,etalon[j8]);
							if(mas[18]!=-1) j9=18;
						}
					}
					j9--;
				}
			}
		}
		printf("Case #%d: %.4d\n",i+1,count);
	}	
	return 0;
}

