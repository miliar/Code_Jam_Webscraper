#include<iostream>
#include<math.h>
//#include<algorithm>
using namespace std;

char map[150];
void init(){
	map[' ']=' ';
	map['a']='y';
	map['b']='h';
	map['c']='e';
	map['d']='s';
	map['e']='o';
	map['f']='c';
	map['g']='v';
	map['h']='x';
	map['i']='d';
	map['j']='u';
	map['k']='i';
	map['l']='g';
	map['m']='l';
	map['n']='b';
	map['o']='k';
	map['p']='r';
	map['q']='z';
	map['r']='t';
	map['s']='n';
	map['t']='w';
	map['u']='j';
	map['v']='p';
	map['w']='f';
	map['x']='m';
	map['y']='a';
	map['z']='q';
	return;
}
int main(){
	//FILE * file=fopen("d:\\a.txt","r");
	int t =0,i=0, j =0;
	char gstr[201],outstr[201];
	init();
	//while(fscanf(file,"%s",buffer)!=EOF){
	//fscanf(file, "%d", &t);
	scanf("%d", &t);
	gets(gstr);
	i =1;
	while(i<=t){
		gets(gstr);
		j = 0;
		//fscanf(file, "%d %d %s", &n, &arity, str);		
		while(gstr[j]){
			outstr[j]= map[gstr[j]];
			j++;
		}
		outstr[j]=0;
		printf("Case #%d: %s\n", i,outstr);
		i++;
	}
	//while(gets(buffer)){
	//fclose(file);
	//getchar();
	//getchar();
	return 0;
}