#include<iostream>

 using namespace std;

 int main()
 {
	 char map[][2] = { {'a','y'}, {'b','h'}, {'c','e'}, {'d','s'}, {'e','o'}, {'f','c'}, {'g','v'}, {'h','x'}, {'i','d'}, {'j','u'}, {'k','i'}, {'l','g'}, {'m','l'}, {'n','b'}, {'o','k'}, {'p','r'}, {'q','z'}, {'r','t'}, {'s','n'}, {'t','w'}, {'u','j'}, {'v','p'},  {'w','f'}, {'x','m'}, {'y','a'}, {'z','q'}};

	 int n,count = 1;
	 cin>>n;
	 getchar();
	 char ch;
cout<<"Case #1: ";
	 //while(n--)
	 //{
		 while((ch=getchar()) != EOF)
		 {
			 if(ch == 10)
			 {
                 n--;
				 count++;
                 if(n>0)
				 cout<<"\nCase #"<< count <<": ";
			 }
			 else if(ch == 32)
				 cout<<ch;
			 else cout<<map[ch-97][1];
		 }
	 //}
 }
