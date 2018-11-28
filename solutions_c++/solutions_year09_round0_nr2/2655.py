#include<iostream>
#include<fstream>
using namespace std;


struct point
{
	int alttitude;
	char letter;
};

void getlowest(point** matrix, int i, int j, int& ni, int& nj, int sizei, int sizej);

char getletter(point** matrix, int i, int j,char& curl, int sizei, int sizej);


void main()
{
	string dummy;
	fstream file_op("c:\\answers.txt", ios::out);
	fstream file_rp("c:\\problem.txt", ios::in);

	//Get the test case
	int TestCase;
	file_rp>>TestCase;

	//Get the matrix
	for(int cnt =0; cnt < TestCase; cnt++)
	{
		char curl = 'a';

		//Input the alttitude
		int j;
		file_rp>>j;
		int i;
		file_rp>>i;
		point **matrix;
		matrix = new point*[j];
		for(int k =0; k < j; k++)
			*(matrix+k) = new point[i];
		for(int cnt1 = 0; cnt1 < j; cnt1++)
			for(int cnt2 = 0; cnt2 < i; cnt2++)
			{
				int temp;
				file_rp>>temp;
				matrix[cnt1][cnt2].alttitude = temp;
				matrix[cnt1][cnt2].letter = '%';
			}

		//Calculate the letter
		for(int cnt1 = 0; cnt1 < j; cnt1++)
			for(int cnt2 = 0; cnt2 < i; cnt2++)
			{
				if(matrix[cnt1][cnt2].letter == '%')
					getletter(matrix,cnt2,cnt1,curl,i,j);
			}
		//Output the result
		file_op<<"Case #"<<(cnt+1)<<":"<<endl;
		for(int cnt1 = 0; cnt1 < j; cnt1++)
		{
			for(int cnt2 = 0; cnt2 < i; cnt2++)
			{
				file_op<<matrix[cnt1][cnt2].letter;
				file_op<<" ";
			}
			file_op<<endl;
		}
		for(int k =0; k < j; k++)
			delete [] matrix[k];
		delete [] matrix;
	}
}

void getlowest(point** matrix, int i, int j, int& ni, int& nj, int sizei, int sizej)
{
	int temp[4];
	if( (j-1) < 0)
		temp[0] = 100;
	else
		temp[0] = matrix[j-1][i].alttitude;
	if( (i-1) < 0)
		temp[1] = 100;
	else
		temp[1] = matrix[j][i-1].alttitude;
	if( (i+1) >= sizei)
		temp[2] = 100;
	else
		temp[2] = matrix[j][i+1].alttitude;
	if( (j+1) >= sizej)
		temp[3] = 100;
	else
		temp[3] = matrix[j+1][i].alttitude;
	
	ni = i;
	nj = j+1;
	if(temp[2] <= temp[3])
	{
		ni = i+1;
		nj = j;
		if(temp[1] <= temp[2])
		{
			ni = i-1;
			nj = j;
			if(temp[0] <= temp[1])
			{
				ni = i;
				nj = j-1;
			}
		}
		else
		{
			if(temp[0] <= temp[2])
			{
				ni = i;
				nj = j-1;
			}
		}
	}
	else
	{
		if(temp[1] <= temp[3])
		{
			ni = i-1;
			nj =j;
			if(temp[0] <= temp[1])
			{
				ni = i;
				nj = j-1;
			}
		}
		else
		{
			if(temp[0] <= temp[3])
			{
				ni = i;
				nj = j-1;
			}
		}
	}
	if(nj >= sizej || nj <0 || ni >= sizei || nj < 0)
	{
		ni = -1;
		nj = -1;
		return;
	}
	if(matrix[nj][ni].alttitude >= matrix[j][i].alttitude)
	{
		ni = -1;
		nj = -1;
	}
}

char getletter(point** matrix, int i, int j,char& curl, int sizei, int sizej)
{
	int ni, nj;
	getlowest(matrix,i,j,ni,nj,sizei,sizej);
	if(ni == -1 && nj == -1)
	{
			matrix[j][i].letter = curl;
			char temp = curl+1;
			curl = temp;
	}
	else
	{
		if(matrix[nj][ni].letter != '%')
			matrix[j][i].letter = matrix[nj][ni].letter;
		else
			matrix[j][i].letter = getletter(matrix,ni,nj,curl,sizei,sizej);
	}

	return matrix[j][i].letter;
}