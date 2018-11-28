#include<iostream>
#include<fstream>
using namespace std;

int main(int argc, char** argv){
	ifstream in("A-small-attempt1.in");
	ofstream out("a.out");

char enc[]=
"ejp mysljylc kd kxveddknmc re jsicpdrysi"
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
"de kr kd eoya kw aej tysr re ujdr lkgc jv";

char dec[]=
"our language is impossible to understand"
"there are twenty six factorial possibilities"
"so it is okay if you want to just give up";

int bah[26]={0};

for(int i=0;i<strlen(enc);i++){
	if('a'<=enc[i] && 'z'>=enc[i])
		bah[enc[i]-'a']=dec[i];
}

bah['z'-'a']='q';//hinted
bah['q'-'a']='z';//manually

//cout<<"line"<<endl;

//int empty=-1;
//int sum=0;
//
////int tsum1=0,tsum2=0;
//for(int i=0;i<26;i++){
//	if(bah[i]==0){
//		empty=i;
//	}
//	else
//		sum+=(bah[i]-'a');
//	sum-=i;
////	tsum1+='a'+i;
////	tsum2+=bah[i];
//}
//
////cerr<<tsum1<<','<<tsum2<<endl;
//
//bah[empty]=sum+'a';

//for(int i=0;i<strlen(bleh);i++){
//	bah[bleh[i]]++;
//}
//for(int i=0;i<26;i++){
//	cerr<<(char)bah[i]<<endl;
//}

string line;

int t=0;

in>>t;
	getline(in,line);

for(int i=0;i<t;i++){
	out<<"Case #"<<(i+1)<<": ";
	
	getline(in,line);
	
	for(int j=0;j<line.length();j++){
		if(line[j]>='a' && line[j]<='z'){
			line[j]=bah[line[j]-'a'];
		}
	}
	
	out<<line<<endl;
}

	system("pause");
	return 0;
}
