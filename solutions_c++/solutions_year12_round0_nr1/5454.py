#include <string>
#include <stdlib.h>
#include <iostream>
#include <stdio.h>
#include <cstring>
using namespace std;
int main()
{
	   int t,cnt = 0;
	   string::size_type i;
	   string s;
	   freopen("D:\\Download\\A-small-attempt2.in","r",stdin);
				freopen("D:\\Download\\A-small-attempt2.out", "w", stdout);
	   cin>>t;
				getchar();
	   while(t--)
	   {
					   getline(cin,s);
					   for(i = 0; i != s.size(); i++)
					   {
					   switch(s[i]){
								  case'a':s[i] = 'y';break;
										case'b':s[i] = 'h';break;
										case'c':s[i] = 'e';break;
										case'd':s[i] = 's';break;
										case'e':s[i] = 'o';break;
										case'f':s[i] = 'c';break;
								  case'g':s[i] = 'v';break;
								  case'h':s[i] = 'x';break;
								  case'i':s[i] = 'd';break;
								  case'j':s[i] = 'u';break;
								  case'k':s[i] = 'i';break;
								  case'l':s[i] = 'g';break;
								  case'm':s[i] = 'l';break;
								  case'n':s[i] = 'b';break;
								  case'o':s[i] = 'k';break;
								  case'p':s[i] = 'r';break;
								  case'r':s[i] = 't';break;
								  case's':s[i] = 'n';break;
								  case't':s[i] = 'w';break;
								  case'u':s[i] = 'j';break;
								  case'v':s[i] = 'p';break;
								  case'w':s[i] = 'f';break;
								  case'x':s[i] = 'm';break;
								  case'y':s[i] = 'a';break;
									case'q':s[i] = 'z';break;
								 case'z':s[i] = 'q';break;
								  default:break;
										}
										}
								cout<<"Case #"<<++cnt<<": "<<s<<endl;
				}
				system("pause");
				return 0;
}
	   
	   
				 
