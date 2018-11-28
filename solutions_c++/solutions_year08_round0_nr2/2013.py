#include<iostream>
#include<string>
#include<vector>
#include<sstream>
using namespace std;



struct Times
{
	string d;
	string a;
};

vector<Times> A, B;
int casenum;

void sort()
{
	Times temp;

    for (int i = 0; i < (int)(A.size() -1); i++)
    {
		for(int j = 1; j < (int)A.size(); j++)
        {
			if (A[j].d < A[j-1].d)
            {
				temp = A[j];
				A[j] = A[j-1];
				A[j-1] = temp;
            }
        }
    }
	for (int i = 0; i < (int)(B.size() -1); i++)
    {
		for(int j = 1; (int) j < B.size(); j++)
        {
			if (B[j].d < B[j-1].d)
            {
				temp = B[j];
				B[j] = B[j-1];
				B[j-1] = temp;
            }
        }
    }
}

string turn (string s, int t)
{
	int h = (int)(s[0]-48)*10 + (int)(s[1]-48);
	int m = (int)(s[3]-48)*10 + (int)(s[4]-48);
	string str;
	stringstream ss;

	m += t;


	if (m > 60)
	{
		h += m/60;
		m = m%60;
	}

	if (h<10)
		ss << "0" << h << ":";
	else
		ss << h << ":";

	if (m<10)
		ss << "0" << m;
	else
		ss << m;



	str = ss.str();

	return str;
}

Times* getEarliest (string t, int st)
{
	int i=0;
	Times* temp;

	if(t > "23:59")
		return NULL;
	if (st == 0 && A.empty())
		return NULL;
	if (st == 1 && B.empty())
		return NULL;

	else
	{
		if (st == 0)
		{
			while ((unsigned)i < A.size() && A[i].d < t)
				i++;

			if (i == A.size())
				return NULL;

			temp = new Times;
			temp->a=A[i].a;
			temp->d=A[i].d;
			A.erase(A.begin() + i);
			return temp;
		}
		else
		{
			while ((unsigned)i < B.size() && B[i].d < t)
				i++;

			if (i == B.size())
				return NULL;

			temp = new Times;
			temp->a=B[i].a;
			temp->d=B[i].d;
			B.erase(B.begin() + i);
			return temp;
		}
	}
}

void solve(int T)
{
	sort ();
	Times* temp;
	int i =0, j=0, st, st1;
	string cur;

	while (!(A.empty()) || !(B.empty()))
	{
		cur = "00:00";

		
		if (B.empty())
			st = 0;
		else if (A.empty())
			st = 1;
		else if (A[0].d < B[0].d)
			st = 0;
		else
			st = 1;

		st1 = st;

		while ((temp = getEarliest(cur, st1)) != NULL)
		{	
			cur = turn(temp->a, T);
			st1 = (st1+1)%2;
		}
		if (st == 0)
			i++;
		else if (st == 1)
			j++;
	}

	cout << "Case #" << casenum << ": " << i << " " << j << endl;
	
}


void doIt()
{
	casenum = 0;

	int N, T, NA, NB;
	Times temp;

	cin >> N;

	for (int i=0; i<N; i++)
	{
		cin >> T;
		cin >> NA;
		cin >> NB;
		A.clear(); B.clear();

		for (int j=0; j< NA; j++)
		{
			cin >> temp.d;
			cin >> temp.a;


			A.push_back(temp);
		}

		for (int j=0; j<NB; j++)
		{
			cin >> temp.d;
			cin >> temp.a;

			B.push_back(temp);
		}
		casenum = i+1;
		solve(T);
	}
}

void main ()
{
	doIt();
}