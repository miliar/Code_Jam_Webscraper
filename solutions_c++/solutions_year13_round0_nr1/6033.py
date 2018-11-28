# include <iostream>
# include <fstream>
# include <string>
using namespace std;
bool check(string s,char p)
{
	if ((s[0]==p || s[0]=='T') && (s[1]==p || s[1]=='T') && (s[2]==p || s[2]=='T') && (s[3]==p || s[3]=='T'))
		return 1;
	else
		return 0;
}
bool checkd(string s1,string s2,string s3,string s4,char p)
{
if (((s1[0]==p || s1[0]=='T') && (s2[1]==p || s2[1]=='T') && (s3[2]==p || s3[2]=='T') && (s4[3]==p || s4[3]=='T')) ||((s4[0]==p || s4[0]=='T') && (s3[1]==p || s3[1]=='T') && (s2[2]==p || s2[2]=='T') && (s1[3]==p || s1[3]=='T')))
	return 1;
else
	return 0;
}
bool checkv(string s1,string s2,string s3,string s4,char p)
{
for (int i=0;i<4;i++)
{
	if ((s1[i]==p || s1[i]=='T') && (s2[i]==p || s2[i]=='T') && (s3[i]==p || s3[i]=='T') && (s4[i]==p || s4[i]=='T')) 
		return 1;

}
return 0;

}
int main()
{
	ofstream fout("large-a.txt");
int t;
bool game_over=0;
bool X_win=0;
bool O_win=0;
bool TIE=0;
cin>>t;
for (int i=0;i<t;i++)
{
game_over=0;
X_win=0;
O_win=0;
TIE=0;
string s1,s2,s3,s4;
cin>>s1>>s2>>s3>>s4;
if (s1.length()==4)
{
if (check(s1,'X')==1 || check(s2,'X')==1 || check(s3,'X')==1 || check(s4,'X')==1 || checkd(s1,s2,s3,s4,'X')==1 || checkv(s1,s2,s3,s4,'X'))
	X_win=1;
if (check(s1,'O')==1 || check(s2,'O')==1 || check(s3,'O')==1 || check(s4,'O')==1 || checkd(s1,s2,s3,s4,'O')==1 || checkv(s1,s2,s3,s4,'O'))
	O_win=1;



if (O_win==1)
	fout<<"Case #"<<i+1<<": O won"<<endl;
else if (X_win==1)
	fout<<"Case #"<<i+1<<": X won"<<endl;
else
{
	for (int i=0;i<4;i++)
	{
		if (s1[i]=='.' || s2[i]=='.' || s3[i]=='.' || s4[i]=='.')
		{
		game_over=1;
		break;
		}

	}
	if (game_over==1)
		fout<<"Case #"<<i+1<<": Game has not completed"<<endl;
	else
		fout<<"Case #"<<i+1<<": Draw"<<endl;


}
}
else
	i--;
}






}