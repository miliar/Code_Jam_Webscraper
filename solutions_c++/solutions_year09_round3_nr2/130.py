#include<iostream>
#include<fstream>
#include<cmath>
#include<vector>
#include<iomanip>
using namespace std;
struct Vector
{
	double X,Y,Z;
};
Vector Center(vector<Vector> &Ps)
{
	Vector V;
	V.X = 0;
	V.Y = 0;
	V.Z = 0;
	int N = Ps.size();
	for(int i=0;i<Ps.size();i++)
	{
		V.X += Ps[i].X/N;
		V.Y += Ps[i].Y/N;
		V.Z += Ps[i].Z/N;
	}
	
	return V;
}

double Dist(const Vector &V)
{
	return sqrt((V.X)*V.X  + (V.Y)*V.Y + (V.Z)*V.Z);
}
double GetCenter(vector<Vector> &Ps,vector<Vector> & Dir,double T,bool R)
{
	vector<Vector> V;
	for(int i=0;i<Ps.size();i++)
	{
		Vector VV;
		VV.X = Ps[i].X + T * Dir[i].X;
		VV.Y = Ps[i].Y + T * Dir[i].Y;
		VV.Z = Ps[i].Z + T * Dir[i].Z;
		V.push_back(VV);
	}

	double D;
	
		D= -Dist(Center(V));
	return D;
}

double BinarySearch(vector<Vector> &Ps,vector<Vector> &Dir,double & D)
{
	if(fabs(Dir[0].X) <= 0.0000000001 && fabs(Dir[0].Y)<=0.00000000001 && fabs(Dir[0].Z) <= 0.00000000001)
	{
		D = -Dist(Ps[0]);
		return 0;
	}
	double Max = ((long long)3000000)  ;
	double Min = 0;
	while(Max - Min >= 0.0000000009)
	{
		double Right = (Max * 2 + Min)/3;
		double Left = (Max + Min * 2)/3;
		if(GetCenter(Ps,Dir,Left,false)>GetCenter(Ps,Dir,Right,false))
			Max = Right;
		else
			Min = Left;
	}
	D=GetCenter(Ps,Dir,(Min+Max)/2,true);
	return Min;
}
int main()
{
	ifstream cin("d:\\CodeJam.in");
	ofstream cout("d:\\CodeJam.out");
	int N;
	cin>>N;
	for(int Case = 1; Case<=N;Case++)
	{
		vector<Vector> Ps,Dr;
		Vector V1,V2;
		int K;
		cin>>K;
		Vector Pos,Dir;
		Pos.X = 0;
		Pos.Y = 0;
		Pos.Z = 0;
		Dir = Pos;
		for(int i=0;i<K;i++)
		{
		cin>>V1.X>>V1.Y>>V1.Z;
		cin>>V2.X>>V2.Y>>V2.Z;
		Dir.X += V2.X/K;
		Dir.Y += V2.Y/K;
		Dir.Z += V2.Z/K;
		Pos.X +=V1.X/K;
		Pos.Y += V1.Y/K;
		Pos.Z += V1.Z/K;
		}
		
		Ps.push_back(Pos);
		Dr.push_back(Dir);
		double T,D;
		T = BinarySearch(Ps,Dr,D);
		cout<<"Case #"<<Case<<": "<<-D<<" "<<T<<endl;
	}
}