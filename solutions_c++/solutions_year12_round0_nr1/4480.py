#include<iostream>
#include<cstdio>
#include<string>
using namespace std;

int n;
string s;

int main()
{
 scanf("%d",&n);
 getline(cin,s);
 for (int i=0;i<n;i++)
 {
   getline(cin,s);
   cout << "Case #"<<i+1<<":"<<" ";
   for (int j=0;j<s.size();j++)
   {        
		    if(s[j]==' ')cout << " ";
            if(s[j]=='a'){cout << 'y';}
            if(s[j]=='b'){cout << 'h';}
            if(s[j]=='c'){cout << 'e';}
            if(s[j]=='d'){cout << 's';}
            if(s[j]=='e'){cout << 'o';}
            if(s[j]=='f'){cout << 'c';}
            if(s[j]=='g'){cout << 'v';}
            if(s[j]=='h'){cout << 'x';}
            if(s[j]=='i'){cout << 'd';}
            if(s[j]=='j'){cout << 'u';}
            if(s[j]=='k'){cout << 'i';}
            if(s[j]=='l'){cout << 'g';}
            if(s[j]=='m'){cout << 'l';}
            if(s[j]=='n'){cout << 'b';}
            if(s[j]=='o'){cout << 'k';}
            if(s[j]=='p'){cout << 'r';}
            if(s[j]=='q'){cout << 'z';}
            if(s[j]=='r'){cout << 't';}
            if(s[j]=='s'){cout << 'n';}
            if(s[j]=='t'){cout << 'w';}
            if(s[j]=='u'){cout << 'j';}
            if(s[j]=='v'){cout << 'p';}
            if(s[j]=='w'){cout << 'f';}
            if(s[j]=='x'){cout << 'm';}
            if(s[j]=='y'){cout << 'a';}
            if(s[j]=='z'){cout << 'q';}
            
   }   
   cout << endl;
  }

//system ("pause");
return 0;	
}
