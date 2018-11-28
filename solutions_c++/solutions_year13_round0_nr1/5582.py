#include <iostream>
#include <cstring>
using namespace std;
int tsts;
string a[4];
void WIN(char x,int qq)
{
	cout << "Case #" << qq << ": " << x << " won\n";
}
bool check()
{
	int cx=0,cy=0;
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		{
			if(a[i][j]=='X')
				cx++;
			if(a[i][j]=='O')
				cy++;
		}
	if(cx-cy<=1 && cx-cy>=0)
		return false;
	return true;
}
int main()
{
	cin >> tsts;
	for(int qq=1;qq<=tsts;qq++)
	{
		for(int i=0;i<4;i++)
			cin >> a[i];
		bool ff=false;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if(a[i][j]=='.')
					ff=true;
		int xt=-1,yt=-1;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if(a[i][j]=='T')
					xt=i,yt=j;
		bool flag=true;
		//satri XX
		for(int i=0;i<4;i++)
		{
			flag=true;
			for(int j=0;j<4;j++)
				if(a[i][j]!=a[i][0])
					flag=false;
			if(flag && a[i][0]!='.')
			{
				WIN(a[i][0],qq);
				break;
			}
			flag=false;
		}
		if(flag)
			continue;
		//sotoni XX
		for(int i=0;i<4;i++)
		{
			flag=true;
			for(int j=0;j<4;j++)
				if(a[j][i]!=a[0][i])
					flag=false;
			if(flag && a[0][i]!='.')
			{
				WIN(a[0][i],qq);
				break;
			}
			flag=false;
		}
		if(flag)
			continue;
		//satri XT
		if(xt!=-1)
		{
			int ttt=0;
			if(yt==0)
				ttt=1;
			flag=true;
			for(int i=0;i<4;i++)
				if(i!=yt)
					if(a[xt][i]!=a[xt][ttt])
						flag=false;
			if(flag&&a[xt][ttt]!='.')
			{
				WIN(a[xt][ttt],qq);
				continue;
			}
		}
		//sotoni XT
		if(xt!=-1)
		{
			int ttt=0;
			if(yt==0)
				ttt=1;
			flag=true;
			for(int i=0;i<4;i++)
				if(i!=xt)
					if(a[i][yt]!=a[ttt][yt])
						flag=false;
			if(flag&&a[ttt][yt]!='.')
			{
				WIN(a[ttt][yt],qq);
				continue;
			}
		}
		//ghotri \ XX 
		flag=true;
		for(int i=0;i<4;i++)
			if(a[i][i]!=a[0][0])
				flag=false;
		if(flag && a[0][0]!='.')
		{
			WIN(a[0][0],qq);
			continue;
		}
		//ghotri / XX
		flag=true;
		for(int i=0;i<4;i++)
			if(a[i][3-i]!=a[0][3])
				flag=false;
		if(flag && a[0][3]!='.')
		{
			WIN(a[0][3],qq);
			continue;
		}
		//ghotri \ XT
		if(xt==yt && xt!=-1)
		{
			flag=true;
			a[xt][yt]=a[0][0];
			for(int i=0;i<4;i++)
				if(a[i][i]!=a[0][0])
					flag=false;
			if(flag && a[0][0]!='.')
			{
				WIN(a[0][0],qq);
				continue;
			}
			a[xt][yt]='T';
		}
		//ghotri / XT
		if(xt+yt==3)
		{
			a[xt][yt]=a[0][3];
			flag=true;
			for(int i=0;i<4;i++)
				if(a[i][3-i]!=a[0][3])
					flag=false;
			if(flag && a[0][3]!='.')
			{
				WIN(a[0][3],qq);
				continue;
			}
			a[xt][yt]='T';
		}
		if(ff)
			cout << "Case #" << qq << ": Game has not completed\n";
		else
			cout << "Case #" << qq << ": Draw\n";
	}
	return 0;
}
