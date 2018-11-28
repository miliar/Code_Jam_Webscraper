#include<iostream>
using namespace std;

int win_row(char arrA[4][4])
{
	int i,j,count_1,count_2,flag=0;
	for(i=0;i<4;i++)
	{
		count_1=0;
		count_2=0;
		for(j=0;j<4;j++)
		{	
			if(arrA[i][j]=='X')
				count_1++;
			else if(arrA[i][j]=='O')
				count_2++;
			else if(arrA[i][j]=='T'){
				count_1++;
				count_2++;
			}
			else
				;
		}
		if(count_1==4 || count_2==4)
			break;
	}
	if(count_1==4)
		flag=1;
	else if(count_2==4)
		flag=2;
	else
		flag=0;
	return flag;
}

int win_col(char arrB[4][4])
{
	int i,j,count_1,count_2,flag=0;
	for(i=0;i<4;i++)
	{
		count_1=0;
		count_2=0;
		for(j=0;j<4;j++)
		{	
			if(arrB[j][i]=='X')
				count_1++;
			else if(arrB[j][i]=='O')
				count_2++;
			else if(arrB[j][i]=='T'){
				count_1++;
				count_2++;
			}
			else
				;
		}
		if(count_1==4 || count_2==4)
			break;
	}
	if(count_1==4)
		flag=1;
	else if(count_2==4)
		flag=2;
	else
		flag=0;
	return flag;
}

int win_right_diagonal(char arrC[4][4])
{
	int i,j,count_1=0,count_2=0,flag=0;
	for(i=0;i<4;i++)
	{
		if(arrC[i][i]=='X')
			count_1++;
		else if(arrC[i][i]=='O')
			count_2++;
		else if(arrC[i][i]=='T'){
			count_1++;
			count_2++;
		}
		else
			;
	}
	if(count_1==4)
		flag=1;
	else if(count_2==4)
		flag=2;
	else
		flag=0;
	return flag;
}

int win_left_diagonal(char arrD[4][4])
{
	int i,j,temp=3,count_1=0,count_2=0,flag=0;
	for(i=0;i<4;i++){
		if(arrD[i][temp]=='X')
			count_1++;
		else if(arrD[i][temp]=='O')
			count_2++;
		else if(arrD[i][temp]=='T')
		{
			count_1++;
			count_2++;
		}
		temp--;
	}
	if(count_1==4)
		flag=1;
	else if(count_2==4)
		flag=2;
	else
		flag=0;
	return flag;
}

int draw_incomplete(char arrE[4][4])
{
	int i,j=0,flag=0;
	for(i=0;i<4;i++){
		for(j=0;j<4;j++)
		{
			if(arrE[i][j]=='.')
			{
				flag=1;
				break;
			}
		}
		if(flag==1)
			break;
	}
	return flag;
}

int main()
{
	int t,temp,temp_1,temp_2,temp_3,temp_4,i,j,start=1;
	char arr[4][4];
	cin>>t;
	while(start<=t)
	{
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
				cin>>arr[i][j];
		}
		temp=win_row(arr);
		temp_1=win_col(arr);
		temp_2=win_right_diagonal(arr);
		temp_3=win_left_diagonal(arr);
		temp_4=draw_incomplete(arr);
		if(temp>0)
		{
			if(temp==1)
				cout<<"Case #"<<start<<": X won\n";
			else if(temp==2)
				cout<<"Case #"<<start<<": O won\n";
			else
				;
		}
		else if(temp_1>0)
		{
			if(temp_1==1)
				cout<<"Case #"<<start<<": X won\n";
			else if(temp_1==2)
				cout<<"Case #"<<start<<": O won\n";
			else
				;
		}
		else if(temp_2>0)
		{
			if(temp_2==1)
				cout<<"Case #"<<start<<": X won\n";
			else if(temp_2==2)
				cout<<"Case #"<<start<<": O won\n";
			else
				;
		}
		else if(temp_3>0)
		{
			if(temp_3==1)
				cout<<"Case #"<<start<<": X won\n";
			else if(temp_3==2)
				cout<<"Case #"<<start<<": O won\n";
		}
		else if(temp_4==1)
		{
			cout<<"Case #"<<start<<": Game has not completed\n";
		}
		else
		{
			cout<<"Case #"<<start<<": Draw\n";
		}
		start++;
	}
	return 0;
}