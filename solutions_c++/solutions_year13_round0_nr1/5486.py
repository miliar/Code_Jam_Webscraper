#include<iostream>
using namespace std;
char square[18] = {'.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'};
int checkwin(char square[])
{
    if (square[1] == square[2] && square[2] == square[3] && square[3] == square[4] && square[1]!='.')
	{	if(square[1]=='X')return 1; if(square[1]=='O') return 2;}
	else if (square[5] == square[6] && square[6] == square[7] && square[7] == square[8] && square[5]!='.')
	{	if(square[5]=='X')return 1; if(square[5]=='O') return 2;}
	else if (square[9] == square[10] && square[10] == square[11] && square[11] == square[12] && square[12]!='.')
	{	if(square[9]=='X')return 1; if(square[9]=='O') return 2;}
	else if (square[13] == square[14] && square[14] == square[15] && square[15] == square[16] && square[16]!='.')
	{	if(square[13]=='X')return 1; if(square[13]=='O') return 2;}
    else if (square[1] == square[5] && square[5] == square[9] && square[9] == square[13] && square[13]!='.')
    {	if(square[1]=='X')return 1; if(square[1]=='O') return 2;}
	else if (square[2] == square[6] && square[6] == square[10] && square[10] == square[14] && square[14]!='.')
	{	if(square[2]=='X')return 1; if(square[2]=='O') return 2;}
	else if (square[3] == square[7] && square[7] == square[11] && square[11] == square[15] && square[15]!='.')
	{	if(square[3]=='X')return 1; if(square[3]=='O') return 2;}
	else if (square[4] == square[8] && square[8] == square[12] && square[12] == square[16] && square[16]!='.')
    {	if(square[3]=='X')return 1; if(square[3]=='O') return 2;}
    else if (square[1] == square[6] && square[6] == square[11] && square[11] == square[16] && square[16]!='.')
	{	if(square[1]=='X')return 1; if(square[1]=='O') return 2;}
	else if (square[4] == square[7] && square[7] == square[10] && square[10] == square[13] && square[13]!='.')
	{	if(square[4]=='X')return 1; if(square[4]=='O') return 2;}
	else if (square[1] != '.' && square[2] != '.' && square[3] != '.' && square[4] != '.'
 && square[5] != '.' && square[6] != '.' && square[7] != '.' && square[8] != '.' && square[9] != '.'
 && square[10] != '.' && square[11] != '.' && square[12] != '.' && square[13] != '.' && square[14] != '.'
 && square[15] != '.' && square[16] != '.')
	{	return 0;}
	else
		return -1;
}
int main()
{
    freopen("A-small-attempt2.in","r",stdin);
    freopen("A.in","w",stdout);
    
    int t,k=1,i,y,z,c,j=0,x,w;
    char a[22],b[5][5];
    
    cin>>t;
    cin.ignore();
    
    do
    {            
                  c=1;
                  for(i=0;i<4;i++) 
                     cin>>b[i];    
                  for(i=0;i<4;i++)
                   {
                          for(j=0;j<4;j++)
                                   a[c++]=b[i][j];               
                   } 
                   j=0;
               /*    for(i=1;i<=16;i++)
                   cout<<a[i];
                 */  for(i=1;i<=16;i++)
                   {
                                     if(a[i]=='T')
                                               j=i;
                  }
                  w=checkwin(a);
                 // cout<<"\nw="<<w;
                  if(w==1) cout<<"Case #"<<k<<": X won\n";
                  else if(w==2) cout<<"Case #"<<k<<": O won\n";
                  else
                  {
                                if(j)
                                {
                                     a[j]='X';
                                              y=checkwin(a);
                                     a[j]='O';
                                              z=checkwin(a);
                                     if(y==1 && z!=2)
                                             cout<<"Case #"<<k<<": X won\n";
                                     else if(z==2 && y!=1)
                                             cout<<"Case #"<<k<<": O won\n";
                                     else if(y==-1 && z==-1)
                                             cout<<"Case #"<<k<<": Game has not completed\n";
                                     else if(y==0 && z==0)
                                             cout<<"Case #"<<k<<": Draw\n";
                                }
                                else
                                {
                                    if(w==0) cout<<"Case #"<<k<<": Draw\n";
                                    if(w==-1)cout<<"Case #"<<k<<": Game has not completed\n";
                                }
                  }              
                   
                   
    }while(k++!=t);
    
    
    
    return 0;
}
