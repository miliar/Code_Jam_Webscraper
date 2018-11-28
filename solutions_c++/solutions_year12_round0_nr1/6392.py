# include<iostream>
# include<fstream>

using namespace std;


int main()
{
    
//ifstream cin("A-small-attempt2.in");
//ofstream cout("out.out");

char arr[30];
int T=3;
string frase,result;
arr[0]='y';//a
arr[1]='h';//b
arr[2]='e';//c
arr[3]='s';//d
arr[4]='o';//e
arr[5]='c'; //f
arr[6]='v';//g
arr[7]='x';//h
arr[8]='d';//i
arr[9]='u';//j
arr[10]='i';//k
arr[11]='g';//l
arr[12]='l';//m
arr[13]='b';//n
arr[14]='k';//o
arr[15]='r';//p
arr[16]='z';//q
arr[17]='t';//r
arr[18]='n';//s
arr[19]='w';//t
arr[20]='j';//u
arr[21]='p';//v
arr[22]='f';//w
arr[23]='m';//x
arr[24]='a';//y
arr[25]='q';//z

cin>>T;
cin.ignore();
char a;
for (int i=1;i<=T;i++){
    getline(cin,frase);
    cout<<"Case #"<<i<<": ";
    for(int j=0;j<frase.size();j++){
        a=frase[j];
        if(a>=65 && a<= 90){
          a=arr[(frase[j]+32)-97];
          a -=32;
          cout<<a;
          continue;
          }else if (a>=97 && a<= 122){
                     a=arr[frase[j]-97];
             cout<<a;
             continue;
            }
            cout<<a;
        }
    cout<<endl;
    }

//system("pause");
return 0;


}
/*
b=n//b
c=e//c
d=s
e=o
f=c
g=v
h=b
i=d
j=u
k=i
l=g
m=l
n=b
o=k
p=r
q=z
r=t
s=n
t=w
u=j
v=p
w=f
x=m
y=a
z=q
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv


Output
Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up

*/


