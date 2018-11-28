#include<iostream>
#include<stdio.h>
using namespace std;
int main(){
	int n,i,j;
	char map[26],temp;
	int flag[26];
	for(i=0;i<=25;i++){
		map[i]='#';
	        flag[i]=-1;
	}
	cin >> n;
	map[0]='y';
	flag['y'-'a']=0;
	map['o'-'a']='e';
	flag['e'-'a']=0;
	map['z'-'a']='q';
	flag['q'-'a']=0;
	string in[100],out[100];
	in[1]="ejp mysljylc kd kxveddknmc re jsicpdrysi";
	in[2] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	in[3]="de kr kd eoya kw aej tysr re ujdr lkgc jv";
	out[1]="our language is impossible to understand";
	out[2]="there are twenty six factorial possibilities";
	out[3]="so it is okay if you want to just give up";
	i=0;
	while(i<=3){
		for(j=0;j<in[i].size();j++){
			if(in[i][j]!=' '){
				map[in[i][j]-'a']=out[i][j];	
				flag[out[i][j]-'a']=0;
			}
		}
		i++;
	}
	for(i=0;i<=25;i++)
		if(flag[i]==-1)
			temp=i;
	for(i=0;i<=25;i++)
		if(map[i]=='#'){
			map[i]=temp+'a';
		}
	//for(i=0;i<=25;i++)
	//	cout<<map[i]<<" ";
	int m=0;
        string abc;
	getline(cin,abc);
	while(n--){
		m++;
		string input,output="";
		getline(cin,input);
		for(i=0;i<input.size();i++)
			if(input[i]!=' ')
				output+=map[input[i]-'a'];
			else
			  	output+=input[i];
		cout<<"Case #"<<m<<": "<<output<<endl;
	}
	
}
