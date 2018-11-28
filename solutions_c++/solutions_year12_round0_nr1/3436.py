#include<iostream>
#include<string>
using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
    int i,j,k;
    string a;
    
    cin>>i;
    j=i;
    getline(cin,a);
    while(i--)
    {
              string b;
              getline(cin,a);
              cout<<"Case #"<<j-i<<": ";
              for(k=0;k<a.size();k++)
              {
              if (a[k]=='y') b+='a';
              if (a[k]=='n') b+='b';
              if (a[k]=='f') b+='c';
              if (a[k]=='i') b+='d';
              if (a[k]=='c') b+='e';
              if (a[k]=='w') b+='f';
              if (a[k]=='l') b+='g';
              if (a[k]=='b') b+='h';
              if (a[k]=='k') b+='i';
              if (a[k]=='u') b+='j';
              if (a[k]=='o') b+='k';
              if (a[k]=='m') b+='l';
              if (a[k]=='x') b+='m';
              if (a[k]=='s') b+='n';
              if (a[k]=='e') b+='o';
              if (a[k]=='v') b+='p';
              if (a[k]=='z') b+='q';
              if (a[k]=='p') b+='r';
              if (a[k]=='d') b+='s';
              if (a[k]=='r') b+='t';
              if (a[k]=='j') b+='u';
              if (a[k]=='g') b+='v';
              if (a[k]=='t') b+='w';
              if (a[k]=='h') b+='x';
              if (a[k]=='a') b+='y';
              if (a[k]=='q') b+='z';
              if (a[k]==' ') b+=' ';
              }
              cout<<b<<endl;
    }

    
	return 0;
}
/*a y
b n
c f
d i
e c
f w
g l
h b
i k
j u
k o
l m
m x
n s
o e
p v
q z
r p
s d
t r
u j
v g
w t
x h
y a
z q*/
