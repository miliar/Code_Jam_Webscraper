#include<iostream>
#include<fstream>
#include<locale>
#include<vector>

using namespace std;

int main()
{
	ifstream fin	("D:\\CodingForFun\\google code jam\\2009 1 Qualification\\files\\B1.in");
	ofstream fout	("D:\\CodingForFun\\google code jam\\2009 1 Qualification\\files\\B1.out");


	int T, H, W;

	fin>>T;
	cout<<T<<endl<<endl;

	vector<vector<int> > map1(101);
	vector<vector<int> > map2(101);

	for(int h = 0; h < 100; h++)
	{
		map1[h].resize(101);
		map2[h].resize(101);
	}
	for(int i = 0; i < T; i++)
	{
		fin>>H>>W;
//		cout<<H<<" "<<W<<endl;

		for(int h = 0; h < H; h++)
			for(int w = 0; w < W; w++)
			{
				map2[h][w] = 0;
//				cout<<"w"<<w<<"h"<<h<<" "<<(int)map2[h][w]<<endl;
				int input;
				fin>>input;
				map1[h][w] = input;
//				cout<<"w"<<w<<"h"<<h<<" "<<map1[h][w]<<endl;
			}

		vector<int> arr(10000, -1);

		int index = 1;
		for(int h = 0; h < H; h++)
		{
			for(int w = 0; w < W; w++)
			{
				int min = map1[h][w];

				int* value = 0;

				if(h > 0)	if(min > map1[h-1][w]) {min = map1[h-1][w]; value = &map2[h-1][w]/*'n'*/;}
				if(w > 0)	if(min > map1[h][w-1]) {min = map1[h][w-1]; value = &map2[h][w-1]/*'w'*/;}
				if(w < W-1)	if(min > map1[h][w+1]) {min = map1[h][w+1]; value = &map2[h][w+1]/*'e'*/;}
				if(h < H-1)	if(min > map1[h+1][w]) {min = map1[h+1][w]; value = &map2[h+1][w]/*'s'*/;}

				int t = 0;
				if(min != map1[h][w])
				{
					if(*value == 0 && map2[h][w] == 0)
					{
						t = 1;
						*value = index++;
						map2[h][w] = *value;
					}
					else if(*value == 0 && map2[h][w] != 0)
					{
						t = 2;
						*value = map2[h][w];
					}
					else if(*value != 0 && map2[h][w] == 0)
					{
						t = 3;
						map2[h][w] = *value;
					}
					else
					{
						if(map2[h][w] > *value)
						{
							arr[map2[h][w]] = *value;
						}
						else
						{
							arr[*value] = map2[h][w];
						}
					}
//					cout<<"w"<<w<<"h"<<h<<" "<<t<<endl;
				}
				else if(map2[h][w] == 0)
				{
					map2[h][w] = index++;
				}
//								cout<<t<<map2[0][0]<<" ";
				//				cout<<map2[h][w] ;
			}
//			cout<<endl;
		}
		fout<<"Case #"<< i+1 <<":"<<endl;

		cout<<endl;


		int y = 'a';
		for(int x = 1; x < index; x++)
		{
			if(arr[x] < 0)	{arr[x] = y++;}
			else
			{
				int t = x;
				while(arr[t] > 0)
				{
					t = arr[t];
				}
				arr[x] = t;
			}
//			cout<<arr[x]<<endl;
		}
//		cout<<endl;

		for(int h = 0; h < H; h++)
		{
			for(int w = 0; w < W; w++)
			{
				if(w != 0)fout<<' ';

					cout<<(char)arr[map2[h][w]];
					fout<<(char)arr[map2[h][w]];

			}
			cout<<endl;
			fout<<endl;
		}
	}

	return 0;
}
