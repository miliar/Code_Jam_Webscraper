

#include <stdio.h>
#include <stdlib.h>

#include <vector>
#include <algorithm>
#include <bitset>
#pragma warning(disable : 4996)

using namespace std;
static void ReadIntegerInLine(vector<int> &v, FILE *in);
static int ReadInt(FILE *in);

#define MAX_T 500 //maxim count of cases

int GetLittlePos2(vector<char> &buf, int len, int pos1, char l1)
{
	char l = 10;
	int pos = pos1+1;
	for(int i=pos1+1 ; i<len;  i++)
	{
		if ((buf[i]<l && buf[i]>l1) )
		{
			pos = i;
			l = buf[i];
		}
	}
	return pos;
}


// int GetLittlePos(vector<char> &buf, int len)
// {
// 	char l = 9;
// 	int pos = 0;
// 	for(int i=len-1; i>=0 ; i--)
// 	{
// 		if (buf[i]<l)
// 		{
// 			pos = i;
// 			l = buf[i];
// 		}
// 	}
// 	return pos;
// }

int IsOrdered(vector<char> &buf, int start,int end)
{
	for(int i=start; i<end ; i++)
	{
		if (buf[i]<buf[i+1])
		{
			return false;
		}
	}
	return true;
}
void GetNext(char *data, int len)
{
	vector<char> buf;
	//copy into vector
	for(int i=0; i<len; i++)
		buf.push_back(data[i]-'0');
	vector<char>buf2 = buf;
	int pos1;
	for(pos1=len-2; pos1>=0; pos1--)
	{
		if (!IsOrdered(buf, pos1, len-1))
			break;
	}
	if (pos1==-1  )//add one zero to extend
	{
		pos1 = 0;
		sort(buf.begin(), buf.end());
		len++;
		buf.insert(buf.begin(), 0);
		char pos2 = GetLittlePos2(buf, len, 0, 0);
		char tmp = buf[pos1];
		buf[pos1] = buf[pos2];
		buf[pos2] = tmp;
	}
	else //exchanged some char
	{
		char pos2 = GetLittlePos2(buf, len, pos1, buf[pos1]);
		char tmp = buf[pos1];
		buf[pos1] = buf[pos2];
		buf[pos2] = tmp;
		sort(buf.begin()+pos1+1, buf.end());
	}
	//copy into vector
	int i;
	for(i=0; i<len; i++)
		data[i] = buf[i]+'0';
	data[i] = 0;//string end

}


//process No 'no' case and output the result
bool DoCase(int no, FILE *in, FILE *out)
{
	bool ret = true;
	char buf[22];
	int len;
	//read parameters
	fscanf(in, "%s", buf);
	len = strlen(buf);
	if (len<=0 || len>21)
	{
		printf("bad case number at No. %d cases (%s)\n", no, buf);
		return false;
	}

	//process the case
	if (no==40)
		no = no;
	GetNext(buf, len);

	//output the result if successed
	fprintf(out, "Case #%d: %s\n", no, buf);
	return true;
}

//process all cases, and out put
bool DoAll(FILE *in, FILE *out)
{
	bool ret = true;
	int T = ReadInt(in);
	if (T< 1 || T> MAX_T)
	{
		printf("Bad test case count T:%d\n", T);
		return false;
	}
	for(int i=1; i<=T; i++)
	{
		if (!DoCase(i, in, out))
		{
			printf("No. %d cases failed\n", i);
			ret = false;
			break;
		}
	}
	return ret;
}

void Init()
{
	//
}

void Finalize()
{

}

// ********************************************************
// ******************************************************** 
static void ReadIntegerInLine(vector<int> &v, FILE *in)
{
	int t;
	char c;
	v.clear();
	while(!feof(in))
	{
		fscanf(in, "%d", &t);
		v.push_back(t);
		fread(&c, 1, 1, in);
		if (c==0x0d || c==0x0a)
			break;
		else
			ungetc(c, in);//put back the char 
	}
}

static int ReadInt(FILE *in)
{
	int t;
	fscanf(in, "%d", &t);
	return t;
}

void usage()
{
	printf("jam1b1 in_file out_file\n");
}


int main(int argc, char *argv[])
{

	if (argc!=3)
	{
		printf("Bad parmater\n");
		usage();
		goto failed;
	}

	FILE *in, *out;
	in = fopen(argv[1], "rb");
	if (in==NULL )
	{
		printf("Can not open input file %s", argv[1]);
		goto failed;
	}
	out = fopen(argv[2], "wb");
	if (out == NULL)
	{
		printf("Can not open out file %s", argv[2]);
		goto failed;
	}
	Init();

	if (!DoAll(in, out))
		printf("Failed\n");
	else
		printf("OK\n");
	Finalize();
	fclose(in);
	fclose(out);

failed:
	printf("any key exit...\n");
	getchar();
	return 1;
}
