#include<iostream>
#include<fstream>
using namespace std;
ifstream fin("A-large.in");
ofstream fout("A-large.out");
char c[16];

char check(int i){//only check row and column
	int a=i%4; int b=i/4;
	if((c[0]=='X'||c[0]=='T')&&(c[5]=='X'||c[5]=='T')&&(c[10]=='X'||c[10]=='T')&&(c[15]=='X'||c[15]=='T'))
		return 'X';
	if((c[3]=='X'||c[3]=='T')&&(c[6]=='X'||c[6]=='T')&&(c[9]=='X'||c[9]=='T')&&(c[12]=='X'||c[12]=='T'))
		return 'X';
	if((c[0]=='O'||c[0]=='T')&&(c[5]=='O'||c[5]=='T')&&(c[10]=='O'||c[10]=='T')&&(c[15]=='O'||c[15]=='T'))
		return 'O';
	if((c[3]=='O'||c[3]=='T')&&(c[6]=='O'||c[6]=='T')&&(c[9]=='O'||c[9]=='T')&&(c[12]=='O'||c[12]=='T'))
		return 'O';
	if((c[a]=='X'||c[a]=='T')&&(c[a+4]=='X'||c[a+4]=='T')&&(c[a+8]=='X'||c[a+8]=='T')&&(c[a+12]=='X'||c[a+12]=='T'))
		return 'X';
	if((c[a]=='O'||c[a]=='T')&&(c[a+4]=='O'||c[a+4]=='T')&&(c[a+8]=='O'||c[a+8]=='T')&&(c[a+12]=='O'||c[a+12]=='T'))
		return 'O';
	if((c[4*b]=='X'||c[4*b]=='T')&&(c[4*b+1]=='X'||c[4*b+1]=='T')&&(c[4*b+2]=='X'||c[4*b+2]=='T')&&(c[4*b+3]=='X'||c[4*b+3]=='T'))
		return 'X';
	if((c[4*b]=='O'||c[4*b]=='T')&&(c[4*b+1]=='O'||c[4*b+1]=='T')&&(c[4*b+2]=='O'||c[4*b+2]=='T')&&(c[4*b+3]=='O'||c[4*b+3]=='T'))
		return 'O';
	return 'C';
}

int main(){
	int t,T,i,j;
	fin>>t;
	char result;
	for(T=0;T<t;T++)
	{
		fout<<"Case #"<<T+1<<": ";
		for(i=0;i<16;i++)
			fin>>c[i];
		for(i=0;i<16;i++){
			result=check(i);
			if(result=='C') continue;
			else break;
		}
		if(result=='X'){
			fout<<"X won"<<endl;
			continue;
		}
		else if(result=='O'){
			fout<<"O won"<<endl;
			continue;
		}
		int flag=0;
		for(i=0;i<16;i++)
			if(c[i]=='.'){
				fout<<"Game has not completed"<<endl;
				flag=1;
				break;
			}
		if(flag==1) continue;
		fout<<"Draw"<<endl;
//		getchar();
	}
}