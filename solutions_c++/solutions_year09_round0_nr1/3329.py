# include <iostream>
# include <vector>

using namespace std;
int L,D,N;
vector <string> dic;
void input() {
string stri;
for(int i=0;i<D;i++)
{
cin>>stri;
dic.push_back(stri);
}
}
int search(vector <string> table)
{
     int count=0,i,j;
     int dic_sz=dic.size();
     for ( i=0;i<dic_sz;i++)
     {
     int k=0;
     for (j=0;j<dic[i].size();j++,k++) if (find(table[k].begin(),table[k].end(),dic[i][j])==table[k].end()) break;
     if (j==dic[i].size())
     count++;
     }
     return count;
}

int main()
{
int i=0;
cin>>L>>D>>N;
string str;
string s;
bool bracket=false;
int k=0,j=0,caseno=0,count;
input();
while (N--)
{
caseno++;
cin>>str;
vector<string> table;
string sub;
int str_len =str.length();
i=0;
while(i<str_len)
{
if (str[i]=='(') bracket=true;
else if (str[i]==')')
{
bracket=false;
table.push_back(sub);
sub.erase(sub.begin(),sub.end());
}
else if (bracket==false)
{
s.push_back(str[i]);
table.push_back(s);
}
else if (bracket==true) sub.push_back(str[i]);
i++;
}
count=search(table);
cout<<"Case #"<<caseno<<": "<<count<<endl;
}
return 0;
}
