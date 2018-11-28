#include<iostream>
#include<string>
#include<map>
#include<cstdio>

using namespace std;

typedef map<char, char> in;

int main()
{

freopen("A.in","r",stdin);
freopen("ap.in","w",stdout);
in coll;

coll.insert(make_pair('a','y'));
coll.insert(make_pair('b','h'));
coll.insert(make_pair('c','e'));
coll.insert(make_pair('d','s'));
coll.insert(make_pair('e','o'));
coll.insert(make_pair('f','c'));
coll.insert(make_pair('g','v'));
coll.insert(make_pair('h','x'));
coll.insert(make_pair('i','d'));
coll.insert(make_pair('j','u'));
coll.insert(make_pair('k','i'));
coll.insert(make_pair('l','g'));
coll.insert(make_pair('m','l'));
coll.insert(make_pair('n','b'));
coll.insert(make_pair('o','k'));
coll.insert(make_pair('p','r'));
coll.insert(make_pair('q','z'));
coll.insert(make_pair('r','t'));
coll.insert(make_pair('s','n'));
coll.insert(make_pair('t','w'));
coll.insert(make_pair('u','j'));
coll.insert(make_pair('v','p'));
coll.insert(make_pair('w','f'));
coll.insert(make_pair('x','m'));
coll.insert(make_pair('y','a'));
coll.insert(make_pair('z','q'));
coll.insert(make_pair(' ',' '));

int n;
 in::iterator pos,pos1;

cin>>n;

int k=0;
cin.ignore();

for(k;k<n;k++)
{
       string s1="",b1="";
b1.empty();
s1.empty();
    getline(cin,s1);


 for(int i=0;i<s1.length();i++)
{
for (pos = coll.begin(); pos != coll.end(); ++pos)
{
    if (s1[i]==pos->first)
    {
b1=b1+pos->second ;
    }
}
}

cout<<"Case #"<<k+1<<": "<<b1<<endl;

}


}
