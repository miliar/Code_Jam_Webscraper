#include <iostream>
#include <list>
#include <string>

using namespace std;

typedef struct s_transform {
	char in[2];
	char out;
} transform;

typedef struct s_oppose {
	char in[2];
} oppose;

typedef list<transform> transformlist;
typedef list<oppose> opposelist;
typedef transformlist::const_iterator transformit;
typedef opposelist::const_iterator    opposeit;

static transformlist xlist;
static opposelist    olist;
static char formattedString[1024];

char applytransform(char lt, char rt)
{
	for(transformit k = xlist.begin(); k != xlist.end(); ++k)
	{
		if( (k->in[0] == lt && k->in[1] == rt) ||
			(k->in[0] == rt && k->in[1] == lt) )
			return k->out;
	}

	return 0;	
}

bool applyopposition(char* str, char rt, int strlen)
{
	for(opposeit k = olist.begin(); k != olist.end(); ++k)
	{
		if (k->in[0] == rt) 
		{
			for(int i = 0; i < strlen; ++i)
			{
				if(str[i] == k->in[1])
					return true;
			}
		}
		if( k->in[1] == rt) 
		{
			for(int i = 0; i < strlen; ++i)
			{
				if(str[i] == k->in[0])
					return true;
			}
		}
	}

	return false;	
}

void ProcessResult(int N, char str[101])
{
	char* resultString = (char*) calloc(strlen(str),sizeof(char));
	int  curResult = 0;
	int  curStr    = 0;
	char xformed;
	int  opposed;

	int formatCur = 0;
	for(int curStr = 0; curStr < N; ++curStr)
	{
		// Apply transforms to last 2 chars
		if(curResult > 0)
		{
			xformed = applytransform(resultString[curResult-1],str[curStr]);
			if(xformed)
			{
				resultString[curResult-1] = xformed;
			}
			// Apply oppositions to entire string up to curResult
			else
			{
				opposed = applyopposition(resultString,str[curStr], curResult);
				if(opposed)
				{
					resultString[0]='\0';
					curResult = 0;
				}
				else
				{
					resultString[curResult++] = str[curStr];
				}
			}

			resultString[curResult] = '\0';
		}
		// Nothing happening? Then just copy the char!
		else
		{
			resultString[curResult++] = str[curStr];
			resultString[curResult] = '\0';
		}
	}

	formattedString[formatCur++] = '[';

	for(int i = 0; resultString[i] != '\0'; ++i)
	{
		formattedString[formatCur++] = resultString[i];

		if(resultString[i+1] != '\0') {
			formattedString[formatCur++] = ',';
			formattedString[formatCur++] = ' ';
		}
	}
	formattedString[formatCur++] = ']';
	formattedString[formatCur] = '\0';
	
}

int main(int nargs, char** args)
{
	char result[101];
	char three[4];
	char two[3];

	transform tempTrans;
	oppose    tempOppose;
	
	int T;
	int C;
	int D;
	int N;

	cin >> T;

	for(int t = 1; t <= T; ++t)
	{
		xlist.clear();
		olist.clear();

		cin >> C;

		for(int c = 0; c < C; ++c)
		{
			cin >> three;

			memcpy(tempTrans.in,three,2);
			tempTrans.out = three[2];

			xlist.push_back(tempTrans);
		}

		cin >> D;
		for(int d = 0; d < D; ++d)
		{
			cin >> two;

			memcpy(tempOppose.in,two,2);

			olist.push_back(tempOppose);
		}

		cin >> N >> result;		

		ProcessResult(N, result);

		cout << "Case #" << t << ": " << formattedString << endl;
	}

	return 0;
}