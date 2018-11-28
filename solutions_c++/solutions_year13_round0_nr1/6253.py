#include<iostream>

using namespace std;

int main()
{
int casos, i, j, cont=1, condicao = 0 , jog2 = 0, full =0;
char m[10][10];


cin >> casos;
while(casos--)
{
for(i=1;i<5; i++)
{
for(j=1; j<5; j++)
{
cin >> m[i][j];
}
}

jog2 =0;
condicao = 0;
full =0;

for(i=1; i<5; i++)
{
for(j=1; j<5; j++)
{
if(m[i][j] == '.')
full = 1;
if((m[i][j] == 'X' || m[i][j] == 'T') && (m[i][j+1] == 'X' || m[i][j+1] == 'T') && (m[i][j+2] == 'X' || m[i][j+2] == 'T') && (m[i][j+3] == 'X' || m[i][j+3] == 'T'))
{
condicao = 1;
}

else if((m[i][j] == 'X' || m[i][j] == 'T') && (m[i+1][j+1] == 'X' || m[i+1][j+1] == 'T') && (m[i+2][j+2] == 'X' || m[i+2][j+2] == 'T') && (m[i+3][j+3] == 'X' || m[i+3][j+3] == 'T'))
{
condicao = 1;
}

else if((m[i][j] == 'X' || m[i][j] == 'T') && (m[i+1][j] == 'X' || m[i+1][j] == 'T') && (m[i+2][j] == 'X' || m[i+2][j] == 'T') && (m[i+3][j] == 'X' || m[i+3][j] == 'T'))
{
condicao = 1;
}
else if(j == 1 && i == 4 && (m[i][j] == 'X' || m[i][j] == 'T') && (m[i-1][j+1] == 'X' || m[i-1][j+1] == 'T') && (m[i-2][j+2] == 'X' || m[i-2][j+2] == 'T') && (m[i-3][j+3] == 'X' || m[i-3][j+3] == 'T'))
{
condicao = 1;
}


if((m[i][j] == 'O' || m[i][j] == 'T') && (m[i][j+1] == 'O' || m[i][j+1] == 'T') && (m[i][j+2] == 'O' || m[i][j+2] == 'T') && (m[i][j+3] == 'O' || m[i][j+3] == 'T'))
{
jog2 = 1;
}

else if((m[i][j] == 'O' || m[i][j] == 'T') && (m[i+1][j+1] == 'O' || m[i+1][j+1] == 'T') && (m[i+2][j+2] == 'O' || m[i+2][j+2] == 'T') && (m[i+3][j+3] == 'O' || m[i+3][j+3] == 'T'))
{
jog2 = 1;
}

else if((m[i][j] == 'O' || m[i][j] == 'T') && (m[i+1][j] == 'O' || m[i+1][j] == 'T') && (m[i+2][j] == 'O' || m[i+2][j] == 'T') && (m[i+3][j] == 'O' || m[i+3][j] == 'T'))
{
jog2 = 1;
}
else if(j == 1 && i == 4 && (m[i][j] == 'O' || m[i][j] == 'T') && (m[i-1][j+1] == 'O' || m[i-1][j+1] == 'T') && (m[i-2][j+2] == 'O' || m[i-2][j+2] == 'T') && (m[i-3][j+3] == 'O' || m[i-3][j+3] == 'T'))
{
jog2 = 1;
}


}
}

if(jog2 == 1 && condicao == 1)
cout << "Case #" << cont << ": Draw" << endl;
else if(jog2 == 1 && condicao == 0)
cout << "Case #" << cont << ": O won" << endl;
else if(jog2 == 0 && condicao == 1)
cout << "Case #" << cont << ": X won" << endl;
else if(full == 1)
cout << "Case #" << cont << ": Game has not completed" << endl;
else
cout << "Case #" << cont << ": Draw" << endl;

cont++;
}

return 0;
}
