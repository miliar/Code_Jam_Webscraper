// CodeJam 2009 - Round1C_B
// Autor: Benjamín de la Fuente Ranea

#include <Windows.h>
#include <stdarg.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>

using namespace std;

//-------------------------------------------------------------------------
void log(const char* fmt, ...)
{
    const unsigned MAX_LINE_BUFFER = 512;
    char    buf[MAX_LINE_BUFFER];			// Is supposed that MAX_LINE_BUFFER characters are enough.
    va_list arg;
    va_start(arg, fmt);
    vsprintf_s<MAX_LINE_BUFFER>(buf, fmt, arg);
    va_end(arg);
    printf(buf);
    OutputDebugStr(buf);
}

//-------------------------------------------------------------------------
unsigned findLowest(const string& number, unsigned curNdx)
{
    unsigned lowestDigit = 9;
    unsigned ndx = 0;
    for (unsigned i = 0; i < number.length() - curNdx; ++i)
    {
        unsigned curDigit = number[i] - '0';
        if (curDigit <= lowestDigit)
        {
            lowestDigit = curDigit;
            ndx = i;
        }
    }

    return ndx;
}

//-------------------------------------------------------------------------
int findNextNdx(const string& _number, unsigned _ndx)
{
    unsigned value = _number[_ndx] - '0';
    for (unsigned i = _ndx; i > 0; --i)
    {
        unsigned curDigit = _number[i] - '0';
        if (curDigit < value)
            return i;
    }

    return -1;
}

struct TFirefly
{
    TFirefly()
    {
        pos[0] = 0;
        pos[1] = 0;
        pos[2] = 0;
        vel[0] = 0;
        vel[1] = 0;
        vel[2] = 0;
    }
    TFirefly(double x, double y, double z, double vx, double vy, double vz)
    {
        pos[0] = x;
        pos[1] = y;
        pos[2] = z;
        vel[0] = vx;
        vel[1] = vy;
        vel[2] = vz;
    }
    TFirefly(const TFirefly& f)
    {
        pos[0] = f.pos[0];
        pos[1] = f.pos[1];
        pos[2] = f.pos[2];
        vel[0] = f.vel[0];
        vel[1] = f.vel[1];
        vel[2] = f.vel[2];
    }

    TFirefly    operator /(double n)            const   {   return TFirefly(pos[0]/n, pos[1]/n, pos[2]/n, vel[0]/n, vel[1]/n, vel[2]/n);  }
    TFirefly&   operator +=(const TFirefly& f)
    {
        pos[0]+=f.pos[0];
        pos[1]+=f.pos[1];
        pos[2]+=f.pos[2];

        vel[0]+=f.vel[0];
        vel[1]+=f.vel[1];
        vel[2]+=f.vel[2];

        return *this;
    }

    double pos[3];
    double vel[3];
};

double dot(double p1[3], double p2[3])
{
    return p1[0] * p2[0] + p1[1] * p2[1] + p1[2] * p2[2];
}

void normalize(double n[3])
{
    double length = sqrt(dot(n, n));
    n[0] /= length;
    n[1] /= length;
    n[2] /= length;
}

struct	TPlane
{
    //-- constructor ··········································································
    TPlane( double _normal[3],					/// construct a plane from a point of the plane 
            double  _point[3]	) 				/// and plane normal.
    {
        data[0] = _normal[0];
        data[1] = _normal[1];
        data[2] = _normal[2];
        data[3] = -(dot(_normal, _point));
    }

    double dist(double pos[3])
    {
        return data[0]*pos[0] + data[1]*pos[1] + data[2]*pos[2] + data[3];
    }

    bool intersect(double dir[3], double pos[3], double& t)
    {
        double normal[3] = {data[0], data[1], data[2]};
        double projection = -dot(normal, dir);
        if (fabs(projection) < 0.00001)
            // Recta paralela al plano
            return false;

        double distance = dist(pos);
        t = distance / projection;

        return true;
    }

    double data[4];
};

//-------------------------------------------------------------------------
int main(int argc, const char* argv[])
{
    if (argc != 3)
    {
        log("Error: Usage %s [INPUT_FILE] [OUTPUT_FILE]\n", argv[0]);
        return 1;
    }

    ifstream fin(argv[1]);
    ofstream fout(argv[2]);
    
    unsigned T;
    fin >> T;

    for (unsigned t = 0; t < T; ++t)
    {
        fout.setf(ios_base::dec);
        fout << "Case #" << t+1 << ": ";

        unsigned N;
        fin >> N;
        
        TFirefly average;
        for (unsigned n = 0; n < N; ++n)
        {
            TFirefly cur;
            fin >> cur.pos[0] >> cur.pos[1] >> cur.pos[2] >> cur.vel[0] >> cur.vel[1] >> cur.vel[2];
            average += cur / N;
        }

#define TOLERANCE 0.000001
        double t = 0;
        if (abs(average.vel[0]) > TOLERANCE || abs(average.vel[1]) > TOLERANCE || abs(average.vel[2]) > TOLERANCE)
        {
            // Calculate distance from line 'average' to origin
            TFirefly normalizedVel(average);
            normalize(normalizedVel.vel);
            double zero[3] = {0, 0, 0};
            TPlane plane(normalizedVel.vel, zero);
            bool bIntersect = plane.intersect(normalizedVel.vel, average.pos, t);
            if (!bIntersect)
                log("Error");

            t /= sqrt(dot(average.vel, average.vel));
            if (t < 0)
                t = 0;
        }

        double intPto[3] = { average.pos[0] + average.vel[0] * t,
            average.pos[1] + average.vel[1] * t, 
            average.pos[2] + average.vel[2] * t};

        double distance = sqrt(dot(intPto, intPto));
        fout.setf(ios_base::fixed);
        fout.precision(8);
        fout << distance << " " << t << endl;
    }

    fout.close();

    return 0;
}
