
#include <fstream>
#include <strstream>
#include <iostream>
#include <typeinfo>
#include <vector>
#include <string>
#include <cmath>
#include <cstdio>
#include <algorithm>

using namespace std;

int err(ofstream& fout, char* name = 0, int* param = 0)
{
	ostrstream msg;
	msg << "Error! ";
	msg << (name? name: "param");
	msg << " is ";
	param? msg << *param: msg << "wrong";
	cout << msg.str() << endl;
	fout << msg.str() << endl;
	return 0;
}

/*	template

	static _case= 1;
	string number;
	string src;
	string dst;

	fin>>number>>src>>dst;

	if ()
	{
		cout<<"Error!" << " value is " << value << endl;
		fout<<"Error!" << " value is " << value << endl;
	}

	cout<<"Case #"<<_case<<": "<<_out<<endl;
	fout<<"Case #"<<_case<<": "<<_out<<endl;
	_case++;
	return 0;
*/


#define min(a, b) a<=b?a:b


inline double log2(double x)
{
  static const double xxx = 1.0/log(2.0);
  return log(x)*xxx;
};

int minutes(string hour)
{
	int h;
	int m;
	sscanf(hour.c_str(), "%d:%d", &h, &m);
	return h*60+m;
};
/*
int program(ifstream& fin, ofstream& fout)
{
	static _case= 1;
//	string seq1;
//	string seq2;
//	string dst;

	int rest;
	int NAB, NBA;
	string dep;
	string arr;

	fin>>rest;
	fin>>NAB>>NBA;


	string _out;

	cout<<"Case #"<<_case<<": "<< trA <<" "<<trB<<endl; 
	fout<<"Case #"<<_case<<": "<< trA <<" "<<trB<<endl;
	_case++;
	return 0;
}
*/

int program(ifstream& fin, ofstream& fout)
{
	static _case= 1;
//	string seq1;
//	string seq2;
//	string dst;

	int rest;
	int NAB, NBA;
	string dep;
	string arr;

	fin>>rest;
	fin>>NAB>>NBA;

	vector <int> depA;
	vector <int> arrA;
	vector <int> depB;
	vector <int> arrB;

	int trA= 0;
	int trB= 0;

	for (int i=0; i<NAB; ++i)
	{
		fin>>dep>>arr;
		depA.push_back(minutes(dep));
		arrB.push_back(minutes(arr));
	}
	for (int j=0; j<NBA; ++j)
	{
		fin>>dep>>arr;
		depB.push_back(minutes(dep));
		arrA.push_back(minutes(arr));
	}

	sort(depA.begin(), depA.end());
	sort(depB.begin(), depB.end());
	sort(arrA.begin(), arrA.end());
	sort(arrB.begin(), arrB.end());

	int maxA=0;
	int maxB=0;

	string day("23:59");
	int maxt= minutes(day);
	for (int t=0; t<maxt; ++t)
	{
		while(arrA.size() && ((arrA[0] + rest) ==t))
		{
			trA--;
			arrA.erase(&arrA[0]);
		}
		while (arrB.size() && ((arrB[0] + rest) ==t))
		{
			trB--;
			arrB.erase(&arrB[0]);
		}
		while (depA.size() && depA[0]==t)
		{
			trA++;
//			if (trA>0) maxA++;
			depA.erase(&depA[0]);
		}
		while (depB.size() && depB[0]==t)
		{
			trB++;
//			if (trB>0) maxB++;
			depB.erase(&depB[0]);
		}
		maxA= (maxA<trA)? trA: maxA;
		maxB= (maxB<trB)? trB: maxB;
	}
	string _out;

	cout<<"Case #"<<_case<<": "<< maxA <<" "<<maxB<<endl; 
	fout<<"Case #"<<_case<<": "<< maxA <<" "<<maxB<<endl;
	_case++;
	return 0;
}


int main(int argc, char* argv[])
{
	if (argc==2 && argv[1])
	{
		ifstream fin(argv[1]);
		if (!fin.is_open()) return 1;
		string path(argv[1]);
		unsigned int pos= path.rfind(".");
		path.replace(pos, 4, ".out");
		ofstream fout(path.c_str());
		if (!fout.is_open())
		{
			fin.close();
			return 1;
		}
		int n_o_lines=0;
		fin>>n_o_lines;
		for (int p=0; p<n_o_lines; ++p) program(fin, fout);
		fin.close();
		fout.close();
	}
	return 0;
}

/*

int minutes(string hour)
{
	int h;
	int m;
	sscanf(hour.c_str(), "%d:%d", &h, &m);
	return h*60+m;
};

int program(ifstream& fin, ofstream& fout)
{
	static _case= 1;
//	string seq1;
//	string seq2;
//	string dst;

	int rest;
	int NAB, NBA;
	string dep;
	string arr;

	fin>>rest;
	fin>>NAB>>NBA;

	vector <int> depA;
	vector <int> arrA;
	vector <int> depB;
	vector <int> arrB;

	int trA= 0;
	int trB= 0;

	for (int i=0; i<NAB; ++i)
	{
		fin>>dep>>arr;
		depA.push_back(minutes(dep));
		arrB.push_back(minutes(arr));
	}
	for (int j=0; j<NBA; ++j)
	{
		fin>>dep>>arr;
		depB.push_back(minutes(dep));
		arrA.push_back(minutes(arr));
	}

	sort(depA.begin(), depA.end());
	sort(depB.begin(), depB.end());
	sort(arrA.begin(), arrA.end());
	sort(arrB.begin(), arrB.end());

	int maxA=0;
	int maxB=0;

	string day("23:59");
	int maxt= minutes(day);
	for (int t=0; t<maxt; ++t)
	{
		if (arrA.size() && ((arrA[0] + rest) ==t))
		{
			trA--;
			arrA.erase(&arrA[0]);
		}
		if (arrB.size() && ((arrB[0] + rest) ==t))
		{
			trB--;
			arrB.erase(&arrB[0]);
		}
		if (depA.size() && depA[0]==t)
		{
			trA++;
			depA.erase(&depA[0]);
		}
		if (depB.size() && depB[0]==t)
		{
			trB++;
			depB.erase(&depB[0]);
		}
		maxA= (maxA<trA)? trA: maxA;
		maxB= (maxB<trB)? trB: maxB;
	}
	string _out;

	cout<<"Case #"<<_case<<": "<< trA <<" "<<trB<<endl; 
	fout<<"Case #"<<_case<<": "<< trA <<" "<<trB<<endl;
	_case++;
	return 0;
}

class Vec
{
	int vec[2];
public:

	Vec() {};
	Vec(int x, int y) {vec[0]=(x); vec[1]= y;};
	Vec operator = (const Vec& asn)
	{
		vec[0]= asn.vec[0];
		vec[1]= asn.vec[1];
		return *this;
	};
	bool operator == (const Vec& eq)	{return vec[0]==eq.vec[0] && vec[1]==eq.vec[1];};
	Vec operator + (const Vec& add)		{return Vec(vec[0]+add.vec[0], vec[1]+add.vec[1]);};
	Vec operator - (const Vec& add)		{return Vec(vec[0]-add.vec[0], vec[1]-add.vec[1]);};
	Vec operator += (const Vec& add)
	{
		vec[0]+= add.vec[0];
		vec[1]+= add.vec[1];
		return *this;
	};
	Vec operator -= (const Vec& add)
	{
		vec[0]-= add.vec[0];
		vec[1]-= add.vec[1];
		return *this;
	};
	int operator * (const Vec& ft) {return vec[0] * ft.vec[0] + vec[1] * ft.vec[1];};
	void RotateL() {Vec res(*this * Vec(0, -1), *this * Vec(1, 0)); *this = res;};
	void RotateR() {Vec res(*this * Vec(0, 1), *this * Vec(-1, 0)); *this = res;};

	int GetX() const {return vec[0];};
	int GetY() const {return vec[1];};
};

class Cell
{
	Vec pos;

public:

	Cell(Vec& _pos) {pos= _pos; walls.value = 0;};
	bool IsAtPos(Vec& _pos) {return pos== _pos;};

	void SetDir(Vec& dir)
	{
		if (!walls.dir.north)	walls.dir.north	= dir == Vec(0, 1);
		if (!walls.dir.east)	walls.dir.east	= dir == Vec(1, 0);
		if (!walls.dir.south)	walls.dir.south	= dir == Vec(0, -1);
		if (!walls.dir.west)	walls.dir.west	= dir == Vec(-1, 0);
	};		
	union
	{
		unsigned int value;
		struct
		{
		unsigned north:	1;
		unsigned south:	1;
		unsigned west:	1;
		unsigned east:	1;
		unsigned :		0;
		} dir;
	} walls;
};

class Maze
{
	int min_x; 
	int min_y; 
	int max_x; 
	int max_y; 

	Vec main_pos;
	Vec dir;
	vector<Cell*> path;

public:

	Maze(): main_pos(0, 1), dir(0, -1), min_x (0), min_y (0), max_x (0), max_y (0) {};

	Cell* GetCell(Vec& pos)
	{
		int size= path.size();
		for (int i=0; i<size; ++i)
			if (path[i]->IsAtPos(pos)) return path[i];
		return 0;
	};

	void Move(const char sign)
	{
		switch (sign)
		{
		case 'w':
		case 'W':
			Goto(dir);
			break;

		case 'l':
		case 'L':
			dir.RotateL();
			break;

		case 'r':
		case 'R':
			dir.RotateR();
			break;
		case '\0':
			Cell* current= GetCell(main_pos);
			if (current) current->SetDir(dir);
			dir.RotateR();
			dir.RotateR();
			break;
		}
	};

	void Goto(Vec& _new)
	{
		Cell* current= GetCell(main_pos);
		if (current) current->SetDir(_new);
		main_pos+=_new;
		if (min_x > main_pos.GetX()) min_x= main_pos.GetX();
		if (min_y > main_pos.GetY()) min_y= main_pos.GetY();
		if (max_x < main_pos.GetX()) max_x= main_pos.GetX();
//		if (max_y < main_pos.GetX()) max_x= main_pos.GetY();
		if (!GetCell(main_pos)) path.push_back(new Cell(main_pos));
	};					

	Vec GetDims() const {return Vec(max_x-min_x+1, max_y-min_y+1);};
	Vec GetOrg() const {return Vec(min_x, max_y);};
	int GetIJValue(int i, int j) {return GetCell(GetOrg() + Vec(i, -j))->walls.value;};
};

int program(ifstream& fin, ofstream& fout)
{
	static _case= 1;
	string seq1;
	string seq2;
	string dst;

	fin>>seq1>>seq2;

	Maze maze;
	for (int m=0; seq1[m]; ++m) if (seq1[m+1]) maze.Move(seq1[m]); else maze.Move('\0');
	for (int n=1; seq2[n]; ++n) if (seq2[n+1]) maze.Move(seq2[n]); else maze.Move('\0');

	fout<<"Case #"<<_case<<":"<<endl;
	Vec dims= maze.GetDims();
	for (int j=0; j<dims.GetY(); ++j)
	{
		for (int i=0; i<dims.GetX(); ++i)
		{
			char value[2]={0};
			itoa(maze.GetIJValue(i, j), value, 16);
			fout<<value;
			cout<<value;
		}
		fout<<endl;
		cout<<endl;
	}
	
	string _out;
//	cout<<"Case #"<<_case<<": "<<_out<<endl;
//	fout<<"Case #"<<_case<<": "<<_out<<endl;
	_case++;
	return 0;
}


/*
int program2(istream& fin, ostream& fout)
{
	static _case= 1;
	string number;
	string src;
	string dst;

	fin>>number>>src>>dst;

	int value=0;
	int base= src.size();
	int len= number.size();
	for (int i=len-1, power=1; i>=0; --i, power *= base)
	{
		int digit = src.find(number[i]);
		value+= power * digit;
	}
	int base2= dst.size();
	string _out;
	if (value<0) err(fout, "value", &value);
	while(value)
	{
		int digit= value%base2;
		value-=digit;
		value/=base2;
		_out+=dst[digit];
	}
	reverse(_out.begin(), _out.end());
	cout<<"Case #"<<_case<<": "<<_out<<endl;
	fout<<"Case #"<<_case<<": "<<_out<<endl;
	_case++;
	return 0;
}


int program1(char* str, ostream& fout)
{
	static _case= 1;
	char number[50]={0};
	char src[100]={0};
	char dst[100]={0};

	char* p1= strstr(str, " ");
	char* p2= strstr(p1+1, " ");

	memcpy(number, str, p1-str);
	memcpy(src, p1+1, p2-p1-1);
	strcpy(dst, p2+1);
//	sscanf(str, "%49s %99s %99s", number, src, dst);

	__int64 value=0;
	int base= strlen(src);
	int len= strlen(number);
	for (int i=len-1, power=1; i>=0; --i, power *= base)
	{
		char* p = strchr(src, number[i]);
		int digit = p - src;
		value+= power * digit;
	}

	int base2= strlen(dst);
	string _out;
	if (value<0)
	{
		cout<<"Error!"<<endl;//" value is "<<value;
		fout<<"Error!"<<endl;//" value is "<<value;
	}
	while(value)
	{
		int digit= value%base2;
		value-=digit;
		value/=base2;
		_out+=dst[digit];
	}
	reverse(_out.begin(), _out.end());
	cout<<"Case #"<<_case<<": "<<_out<<endl;
	fout<<"Case #"<<_case<<": "<<_out<<endl;
	_case++;
	return 0;
}

/*
int program(string str)
{
	char* dup= strdup(str.c_str());
	string number= strtok(dup)
	string src= strtok(dup)
	string des= strtok(dup)

	token = strtok(dup, " ");
	number= strtok(0, " ");
	src= strtok(0, " ");
	dst= strtok(0, " ");

	


	free (dup);
	return 0;
}

int main(int argc, char* argv[])
{
	if (argc==1 && argv[1])
	{
		ifstream file(argv[1]);
		int n_o_lines=0;
		for (int p=0; p<n_o_lines+1; ++p)
		{
			string str;
			const int size = 10;
			char tok[size+1];
			tok[size+1]=0;
			bool cont= true;
			do
			{
				file.getline(tok, size);
				str+=tok;
				for (int i=0; i<10; ++i) if (!tok[i]) cont= false;
			}
			while (cont);
			if (!p) n_o_lines= atoi(str.c_str());
			else program(str);
		}
	}
	return 0;
}
*/