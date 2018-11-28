#include<iostream>
#include<stdio.h>

using namespace std;

int ans,n,t,b;
int i,j,k,p,q,z;//iteratr
int c1,c2,f,f1,f2;//counter
char ch;
int state[4][4];
int r[4],c[4],tot;
int row[4],col[4];
int d1,d2;
int sol;

int check(int k)
{
    if(k == 3 || k == -3 || k == 4 || k == -4)
    {
        if(k > 0)
			return 1;
		else
			return -1;
    }
    return 0;
}

int rowsum(int p)
{
   int i,sum;
   sum = 0;
   for(i=0;i<4;i++)
    sum += state[p][i];
   return sum;
}
int colsum(int p)
{
   int i,sum;
   sum = 0;
   for(i=0;i<4;i++)
    sum += state[i][p];
   return sum;
}

int calc()
{
    for(i=0;i<4;i++)
    {
        if(r[i] == 4)
        {
			//cout << "\nChecking row["<<i<<"]";
            row[i] = rowsum(i);
            sol = check(row[i]);
            if(sol != 0)
                return sol;
        }
    }
    for(i=0;i<4;i++)
    {
        if(c[i] == 4)
        {
			//cout << "\nChecking col["<<i<<"]";
            col[i] = colsum(i);
			//cout << "\ncolsum["<<i<<"]="<<col[i];
            sol = check(col[i]);
			//cout << "\nsol["<<i<<"]="<<sol;
            if(sol != 0)
                return sol;
        }
    }
    d1 = state[0][0] + state[1][1] + state[2][2] + state[3][3];
    sol = check(d1);
    if(sol != 0)
       return sol;
    d2 = state[0][3] + state[1][2] + state[2][1] + state[3][0];
    sol = check(d2);
    if(sol != 0)
       return sol;
    return 0;
}

int main(){
	cin >> t;
	//cout<<"Total cases:"<<t<<endl;	
    k = 1;
    while(k<=t)
    {
        i = j = 0;        
        tot = 0;
        for(i=0;i<4;i++)
        {
            r[i] = c[i] = 0;
        }
        for(i=0;i<4;i++)
        {            
            for(j=0;j<4;j++)
            {
                cin>>ch;
                if(ch == 'X')
                {
                    state[i][j] = 1;
                    r[i]++;
                    c[j]++;
                    tot++;
                }  
                else if(ch == 'O')
                {
                    state[i][j] = -1;
                    r[i]++;
                    c[j]++;
                    tot++;
                }    
                else if(ch == 'T')
                {
                    state[i][j] = 0;
                    r[i]++;
                    c[j]++;
                    tot++;
                }    
                else
                {
                    state[i][j] = 100;
                }    
            }
        }
        ans = calc();
		cout << "Case #"<<k<<": ";
        if(ans == 1)
            cout<<"X won"<<endl;
        else if(ans == -1)
            cout<<"O won"<<endl;
        else
            {
                if(tot == 16)
                    cout << "Draw"<<endl;
                else
                    cout << "Game has not completed" <<endl;
            }
        k++;
    }
	cin >> p;
    return 0;
}