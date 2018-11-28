#include <iostream>
#include <fstream>
#include <string>

using namespace std;

class ttime
{
	public: 

	int hh, mm;

	void add (int min)
	{
		mm += min;
		hh += mm/60;
		mm %= 60;

//		hh %= 24;
	}
	int less (ttime t)
	{
		if (hh < t.hh)
			return 1;
		if (hh > t.hh)
			return -1;
		if (mm < t.mm)
			return 1;
		if (mm > t.mm)
			return -1;
		return 0;
	}
	void del ()
	{
		hh = 25;
	}
};

void sort (ttime *t, int n)
{
	ttime temp;  
		
	for (int i=0; i<n; i++)
	{
		for (int j=0; j<n-i-1; j++)
		{
			if (t[j].less(t[j+1]) == -1)
			{
				temp = t[j];
				t[j] = t[j+1];
				t[j+1] = temp;
			}
		}
	}
}
			

int main (int argc, char *argv[])
{
	fstream file;
	int N;				//Test Cases
	int TurnTime;
	int NA, NB;

	ttime ReqA[100], AtA[100], ReqB[100], AtB[100];
	int noata, noreqa, noatb, noreqb;

	file.open (argv[1], ios::in);
	
	file >> N;
	for (int i=0; i<N; i++)
	{
		file >> TurnTime;
		file >> NA >> NB;

		noata = noreqa = noatb = noreqb = 0;
		for (int a=0; a<NA; a++)
		{
			file >>ReqA[noreqa].hh;
		        file.get();
			file >> ReqA[noreqa].mm;
			file >>AtB[noatb].hh;
		        file.get();
			file >>AtB[noatb].mm;
			AtB[noatb].add (TurnTime);
			bool flag = true;
			/*for (int x=0; x<noreqa; x++)
			{
				if (ReqA[x].less(ReqA[noreqa]) == 0 && AtB[x].less(AtB[noatb]) == 0)
				{
					flag = false;
					break;
				}
			}*/
			if (flag == true)
			{
				noreqa ++;
				noatb ++;
			}
		}
		sort (ReqA, noreqa);
		sort (AtB, noatb);
		for (int b=0; b<NB; b++)
		{
			file >>ReqB[noreqb].hh;
		        file.get();
			file >> ReqB[noreqb].mm;
			file >>AtA[noata].hh;
		        file.get();
			file >>AtA[noata].mm;
			AtA[noata].add (TurnTime);
			
			bool flag = true;
			/*for (int x=0; x<noreqb; x++)
			{
				if (ReqB[x].less(ReqB[noreqb]) == 0 && AtA[x].less(AtB[noata]) == 0)
				{
					flag = false;
					break;
				}
			}*/
			if (flag == true)
			{
				noreqb ++;
				noata ++;
			}
		}
		sort (ReqB, noreqb);
		sort (AtA, noata);

		

		for (int a=0; a<NA; a++)
		{
			if (noata == 0 || noreqa == 0)
				break;
			for (int b=0; b<NB; b++)
			{
				if (AtA[b].less (ReqA[a]) == 1 || AtA[b].less (ReqA[a]) == 0) {
					noreqa --;
					noata --;
					AtA[b].del();
					break;
				}
			}
		}
		for (int b=0; b<NB; b++)
		{
			if (noatb == 0 || noreqb == 0)
				break;
			for (int a=0; a<NA; a++)
			{
				if (AtB[a].less (ReqB[b]) == 1 || AtB[a].less (ReqB[b]) == 0) {
					noreqb --;
					noatb --;
					AtB[a].del();
					break;
				}
			}
		}
		cout <<"Case #" <<i+1 <<": " <<noreqa <<" " <<noreqb <<endl;
	}
	return 0;
}
