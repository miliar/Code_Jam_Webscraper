
#include <cstring>
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream> 
#include <cmath>
using namespace std;

struct Pos {
  
    float x;
    float y;
    bool xFlip;
    bool yFlip;
        
    bool operator== (const Pos &src){
        return (x==src.x)&&(y==src.y);
    }
    
    bool operator!= (const Pos &src){
        return !((x==src.x)&&(y==src.y));
    }
    
};

float getDist(const Pos &p){
    return sqrt(p.x*p.x + p.y*p.y);;
}

float getAngle(const Pos &p){
    if (p.x==0 && p.y==0){
        return 10;
    }
    return atan2(p.y, p.x);
}


struct Env {
    float X;
    float Y;
    float x;
    float y;
    float D;
};

void iterate(const Env& env, const Pos &cand, vector<Pos> &db, vector<float> &angles){
    vector<Pos>::iterator dbIt;
    
    cout << "Evaluate " << cand.x << ", " << cand.y << "... \n";
    
    // has been here before: abort
    for (dbIt=db.begin();dbIt<db.end();dbIt++){
        if (*dbIt == cand){
            cout << "has been here before\n";
            return;
        }
    }
    
    // out of range: abort
    if (getDist(cand)*2 > env.D){
        cout << "dist too large\n";
        return;
    }
    
    db.push_back(cand);
    float ang = getAngle(cand);
    
    vector<float>::iterator angIt;
    
    bool valid = true;
    for (angIt=angles.begin();angIt<angles.end();angIt++){
        if (*angIt == ang){
            valid = false;
            continue;
        }
    }
    
    if (valid){
        angles.push_back(ang);
        cout << "is valid\n";
    }
    cout << "propagating\n";
    
    Pos newCand;
    
    newCand = cand;
    newCand.xFlip = !cand.xFlip;
    if (!cand.xFlip){
        newCand.x -= env.x;
    }else{
        newCand.x -= (env.X - env.x);
    }
//    cout << "add new: " << newCand.x << ", " << newCand.y << "\n";
    iterate(env, newCand, db, angles);
    
    newCand = cand;
    newCand.xFlip = !cand.xFlip;
    if (!cand.xFlip){
        newCand.x += (env.X - env.x);
    }else{
        newCand.x += env.x;
    }
//    cout << "add new: " << newCand.x << ", " << newCand.y << "\n";
    iterate(env, newCand, db, angles);    
    
    newCand = cand;
    newCand.yFlip = !cand.yFlip;
    if (!cand.yFlip){
        newCand.y -= env.y;
    }else{
        newCand.y -= (env.Y - env.y);
    }
//    cout << "add new: " << newCand.x << ", " << newCand.y << "\n";
    iterate(env, newCand, db, angles);  
    
    newCand = cand;
    newCand.yFlip = !cand.yFlip;
    if (!cand.yFlip){
        newCand.y += (env.Y - env.y);
    }else{
        newCand.y += env.y;
    }
//    cout << "add new: " << newCand.x << ", " << newCand.y << "\n";
    iterate(env, newCand, db, angles); 
}

void hallofmirror(const string &inpFile, const string &outFile){
    
    ifstream in;
    in.open(inpFile.c_str());
    
    ofstream out;
    out.open(outFile.c_str());
    
    int numCases, H, W, D;
    char tmp;
    in >> numCases;

    Env env;
    
    for (int k=0; k<numCases; k++){
        in >> H >> W >> D;
        env.X = W-2;
        env.Y = H-2;
        env.D = D;
        for (int h=0; h<H; h++){
            for (int w=0; w<W; w++){
                in >> tmp;
                if (tmp=='X'){
                    env.x = w+0.5-1;
                    env.y = h+0.5-1;
                }
            }
        }
        Pos cand;
        cand.x = 0;
        cand.y = 0;
        cand.xFlip = false;
        cand.yFlip = false;
        
        vector<Pos> db;
        db.reserve(1000);
        vector<float> angles;
        angles.reserve(1000);
                        
        iterate(env, cand, db, angles);
        
        out << "Case #" << k+1 << ": " << angles.size()-1 << "\n";
    }
    
}


int main(int argc, const char* argv[]){
    
    hallofmirror(string(argv[1]), string(argv[2]));
    
    return 0;
}

