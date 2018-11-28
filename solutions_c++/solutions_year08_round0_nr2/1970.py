
//ohm shri ganeshay namah
# include <iostream.h>
# include <conio.h>
# include <fstream.h>
#include <stdlib.h>
int cases;
void bubble(int arr[][2], int n)
	{
	int i,j,tmp,tmp1;
	for(i=0;i<n-1;i++)//pass
	for(j=0;j<n-i-1;j++)
	if(arr[j][1]>arr[j+1][1])
		{
		tmp=arr[j][1];
		tmp1=arr[j][0];
		arr[j][1]=arr[j+1][1];
		arr[j][0]=arr[j+1][0];
		arr[j+1][1]=tmp;
		arr[j+1][0]=tmp1;
		}
	}
void main()
	{
	clrscr();
	int taround,na,nb;
	char chh[3],chm[3],ch1;
	ifstream fin;
	ofstream fout;
	fin.open("A-small.in");
	fout.open("output.txt");
	fin.seekg(0);
	fin>>cases;
	cout<<cases<<"\n";
	int count=1;
	while(count<=cases)
	{
	if(count==6)
	count=6;
	fin>>taround>>na>>nb;
	cout<<taround<<" "<<na<<"  "<<nb<<"  \n";
	int train[101][2],dep[101][2],arr[101][2];
	for(int i=0;i<na+nb;i++)
		{
		train[i][0]=i<na?1:2;
		train[i][1]=i>=na?1:2;
		dep[i][0]=i;
		arr[i][0]=i;
		fin.get(ch1);
		fin.get(chh,3,':');
		fin.get(ch1);
		fin.get(chm,3,' ');
		dep[i][1]=atoi(chh)*60+atoi(chm);
		fin.get(ch1);
		fin.get(chh,3,':');
		fin.get(ch1);
		fin.get(chm,3,' ');
		arr[i][1]=atoi(chh)*60+atoi(chm)+taround;
		}
	bubble(arr,na+nb);
	bubble(dep,na+nb);

	int astart=0,bstart=0,pa=0,pb=0,dpro=0,apro=0;
	while(apro<na+nb && dpro<na+nb)
	{
	if(dep[dpro][1]<arr[apro][1])
	train[dep[dpro++][0]][0]==1?(pa==0?astart++:pa--):(pb==0?bstart++:pb--);
	else
	train[arr[apro++][0]][1]==1?pa++:pb++;
	}
	if(apro>=na+nb)
		{
		while(dpro<na+nb)
		train[dep[dpro++][0]][0]==1?(pa==0?astart++:pa--):(pb==0?bstart++:pb--);
		}
	else if(dpro>=na+nb)
		{
		while(apro<na+nb)
		train[arr[apro++][0]][1]==1?pa++:pb++;
		}
	cout<<astart<<"    "<<bstart<<"\n";
	fout<<"Case #"<<count<<": "<<astart<<" "<<bstart<<"\n";
	count++;
	}
	fin.close();
	}

