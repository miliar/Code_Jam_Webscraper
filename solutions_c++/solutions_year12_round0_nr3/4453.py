#include<iostream>
#include<string>
#include<stdlib.h>

using namespace std;

void process();
void deal(char []);
int T,A,B,nod,count;


int main(){
    int i;
    cin>>T;
    for(i=0; i<T; i++){
		count=0;
        cin>>A;
		cin>>B;
        cout<<"Case #"<<i+1<<": ";
        process();
		cout<<count;
        if(i!=T-1)
            cout<<endl;
    }

return 0;
}

void process(){
    int temp=A;
    nod=0;
    while(temp){
        temp=temp/10;
        nod++;
    }
    char str1[20];
    char str2[20];
    while(A<=B){
        _itoa_s(A, str2, 10);
        //cout<<str2<<endl;
        strcpy_s(str1,str2);
        strcat_s(str1,str2);
        //cout<<str1<<endl;
        deal(str1);
        A++;
    }
}

void deal(char str1[20]){
    int j,m;
    char strout[20];

    for(j=1; j<nod; j++){
        strncpy_s(strout, str1+j, nod);
        //cout<<"strout: "<<strout<<endl;
		m=_atoi64(strout);
		//cout<<"m: "<<m<<endl;
		if(m>A && m<=B) count++;
    }


}
