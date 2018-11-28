#include "header.h"

vector<string> Split(const string& line, char delim)
{
	string curStr;
	vector<string> tokens;
	char curChar;

	for(int i = 0; i < (int)line.size(); i++)
	{
		curChar = line[i];
		if(curChar == delim)
		{
			tokens.push_back(curStr);
			curStr.clear();
		}
		else
		{
			curStr += curChar;
		}
	}
	if(!curStr.empty())
		tokens.push_back(curStr);
	return tokens;
}

void onee2(string a)
{

	freopen("A-small.in", "rt", stdin);
	freopen("outputOne.txt", "wt", stdout);

	int n;
	scanf("%d", &n);
	For(test, 1, n) {
		int x1, y1, x2, y2, x3, y3;
		scanf("%d%d%d%d%d%d", &x1, &y1, &x2, &y2, &x3, &y3);
		printf("Case #%d: ", test);
		if ((x2-x1)*(y3-y1)-(x3-x1)*(y2-y1) == 0)
			printf("not a triangle\n");
		else {
			int a = sqr(x1-x2)+sqr(y1-y2);
			int b = sqr(x2-x3)+sqr(y2-y3);
			int c = sqr(x1-x3)+sqr(y1-y3);
			if (a == b || a == c || b == c)
				printf("isosceles ");
			else
				printf("scalene ");
			int m[] = {a, b, c};
			sort(m, m+3);
			if (m[2] > m[0]+m[1])
				printf("obtuse triangle\n");
			else if (m[2] == m[0]+m[1])
				printf("right triangle\n");
			else 
				printf("acute triangle\n");
		}
	}

	exit(0);

}

void one()
{
	//freopen("A-small.in", "rt", stdin);
	freopen("A-small-attempt0.in", "rt", stdin);
	freopen("outputOne.txt", "wt", stdout);

	string filename("A-small-attempt0.in");
	ifstream in;
	in.open(filename.c_str());

	int n;
	//scanf("%d", &n);
	string temp;
	getline(in, temp, '\n');
	istringstream iss(temp);
	iss >> n;
	//cout << n << endl;


	Rep(i, n)
	{
		int l;
		getline(in, temp, '\n');
		istringstream iss1(temp);
		iss1 >> l;
		//cout << l << endl;
		
		string str1, str2;
		getline(in, str1, '\n');
		vector<string> v1, v2;
		v1 = Split(str1, ' ');
		getline(in, str2, '\n');
		v2 = Split(str2, ' ');

		vector<int> vi1, vi2;
		Rep(j, v1.size())
		{
			istringstream isst(v1[j]);
			int tmp;
			isst >> tmp;


			vi1.push_back(tmp);

		}
		//cout << "v1:" << v1.size() << endl;
		Rep(j, v2.size())
		{
			istringstream isst2(v2[j]);
			int tmp2;
			isst2 >> tmp2;
			vi2.push_back(tmp2);
		}
		//cout << "v2:" << v2.size() << endl;

		sort(vi1.rbegin(), vi1.rend());
		sort(vi2.begin(), vi2.end());

		int sum = 0;
		Rep(j, v1.size())
		{
			sum += vi1[j] * vi2[j];
			//cout << vi1[j] << "*" << vi2[j] << endl;
		}
		cout << "Case #" << (i + 1) << ": " << sum << endl;
		
	}





}



void main(void)
{
	
	one();

	return;
}