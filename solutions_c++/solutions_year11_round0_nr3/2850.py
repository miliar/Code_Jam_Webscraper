#include <iostream>
#include <cstdlib>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int *piece;
int piece_size;

int cal_answer(int *arr, int arr_size)
{
	int pre=0;
	int Sean = 0, Sean_xor=0, Patrick = 0;
	vector<int> p;
	for(int i=0;i<arr_size;++i)
	{
		Sean += piece[arr[i]-1];
		Sean_xor ^= piece[arr[i]-1];
		if(arr[i] - pre > 1)
			for(int j=pre+1;j<arr[i];++j)
				p.push_back(j);
		pre = arr[i];
	}
	for(int i=pre+1;i<=piece_size;++i)
		p.push_back(i);
	for(int i=0;i<p.size();++i)
		Patrick ^= piece[p[i]-1];
	if(Sean_xor == Patrick)
		return Sean;
	return 0;
}

void combination(int *arr,int n,int m,int now,int k, int &res){
    if (now == m){
		int tmp = cal_answer(arr, m);
		if(tmp > res)
			res = tmp;
    }
    else
        for (int i=k;i<n;++i){
            arr[now] = i+1;
            combination(arr,n,m,now+1,i+1, res);
        }
}

int solve(int *pe, int pe_size)
{
	int res = 0;
	int *arr = new int[pe_size];
	for(int i=1;i<pe_size;++i)
	{
		combination(arr, pe_size, i, 0, 0, res);
	}
	delete [] arr;

	return res;
}

int main(int argc, char argv[])
{
	ifstream ifile("C-small-attempt0.in");
	ofstream ofile("C-small-attempt0.out");

	int case_num, candy_num;
	ifile >> case_num;

	for(int i=0;i<case_num;++i)
	{
		int res = 0;
		ifile >> candy_num;
		piece_size = candy_num;
		piece = new int [piece_size];
		
		for(int j=0;j<candy_num;++j)
			ifile >> piece[j];

		res = solve(piece, candy_num);

		if(res == 0)
			ofile << "Case #" << i+1 << ": NO\n";
		else
			ofile << "Case #" << i+1 << ": " << res;

		delete [] piece;
	}

	ifile.close();
	ofile.close();

	//system("pause");
	return 0;
}

