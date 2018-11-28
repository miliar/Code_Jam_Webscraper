#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cmath>

struct Firefly {
    double x, y, z;
    double vx, vy, vz;
};

std::vector<struct Firefly> fireflies;

void findCOM(double &x, double &y, double &z, const std::vector<struct Firefly> &cfireflies){
    x = 0.0;
    y = 0.0;
    z = 0.0;
    for(unsigned i = 0; i < cfireflies.size(); i++){
        x += cfireflies[i].x;
        y += cfireflies[i].y;
        z += cfireflies[i].z;
    }
    x /= cfireflies.size();
    y /= cfireflies.size();
    z /= cfireflies.size();
}

void findAverageVelocity(double &vx, double &vy, double &vz, const std::vector<struct Firefly> &cfireflies){
    std::vector<struct Firefly> cur_fireflies = cfireflies;

    double pcx = 0.0, pcy = 0.0, pcz = 0.0;
    for(unsigned j = 0; j < 3; j++){
        for(unsigned i = 0; i < cfireflies.size(); i++){
            cur_fireflies[i].x += cfireflies[i].vx;
            cur_fireflies[i].y += cfireflies[i].vy;
            cur_fireflies[i].z += cfireflies[i].vz;
        }

        double cx, cy, cz;
        findCOM(cx, cy, cz, cur_fireflies);
      
        vx = cx - pcx;
        vy = cy - pcy;
        vz = cz - pcz;

        pcx = cx;
        pcy = cy;
        pcz = cz;
    }
}


double findDistance(double x, double y, double z){
    return sqrt(x*x + y*y + z*z);
}

void searchForCOM(double min_t, double max_t, double dt, double &t, double &dist){
    std::vector<struct Firefly> cur_fireflies = fireflies;

 /*   double cx, cy, cz;
    double cvx, cvy, cvz;

    findCOM(cx, cy, cz, cur_fireflies);
    findAverageVelocity(cvx, cvy, cvz, cur_fireflies);
    std::cout << cx << " " << cy << " " << cz << std::endl;
    std::cout << cvx << " " << cvy << " " << cvz << std::endl;
*/

    double pcx = 0.0, pcy = 0.0, pcz = 0.0;
    for(double time = 0.0; time < 100.0; time += 0.5){
        for(unsigned i = 0; i < cur_fireflies.size(); i++){
            cur_fireflies[i].x += 0.5*cur_fireflies[i].vx;
            cur_fireflies[i].y += 0.5*cur_fireflies[i].vy;
            cur_fireflies[i].z += 0.5*cur_fireflies[i].vz;
        }

        double cx, cy, cz;
        findCOM(cx, cy, cz, cur_fireflies);

        pcx = cx;
        pcy = cy;
        pcz = cz;
    }
    
}

double dotProduct(double x0, double y0, double z0, double x1, double y1, double z1){
    return x0*x1 + y0*y1 + z0*z1;
}

void closestPointOnLine(double x0, double y0, double z0, 
                        double x1, double y1, double z1,
                        double &rx, double &ry, double &rz){
    double vx = x1 - x0;
    double vy = y1 - y0;
    double vz = z1 - z0;

    double wx = -x0;
    double wy = -y0;
    double wz = -z0;

    double c1 = dotProduct(wx, wy, wz, vx, vy, vz);
    if(c1 <= 0){
        rx = x0;
        ry = y0;
        rz = z0;
        return;
    }

    double c2 = dotProduct(vx, vy, vz, vx, vy, vz);
    if(c2 <= c1){
        rx = x1;
        ry = y1;
        rz = z1;
        return;
    }

    double b = c1 / c2;
    rx = x0 + b*vx;
    ry = y0 + b*vy;
    rz = z0 + b*vz;

}

int main(int argc, char **argv){
    unsigned num_tests;
    std::cin >> num_tests;
    for(unsigned i = 0; i < num_tests; i++){
        fireflies.clear();

        unsigned num_fireflies;
        std::cin >> num_fireflies;
        for(unsigned j = 0; j < num_fireflies; j++){
            struct Firefly new_firefly;
            std::cin >> new_firefly.x;
            std::cin >> new_firefly.y;
            std::cin >> new_firefly.z;
            std::cin >> new_firefly.vx;
            std::cin >> new_firefly.vy;
            std::cin >> new_firefly.vz;
            fireflies.push_back(new_firefly);
        }

        
        double vx, vy, vz;
        findAverageVelocity(vx, vy, vz, fireflies);

        double cx, cy, cz;
        findCOM(cx, cy, cz, fireflies);

        double prx = cx + vx * 1000.0;
        double pry = cy + vy * 1000.0;
        double prz = cz + vz * 1000.0;

        //std::cout << cx << " " << cy << " " << cz << std::endl;
        //std::cout << vx << " " << vy << " " << vz << std::endl;

        double rx, ry, rz;
        closestPointOnLine(cx, cy, cz, prx, pry, prz, rx, ry, rz);
        
        
        double t;
        if(fabs(vx) > 0.0001){
           t = (rx-cx)/vx;
        }
        else if(fabs(vy) > 0.0001){
           t = (ry-cy)/vy;
        }
        else{
           t = (rz-cz)/vz;
        }

        if(t != t){
            t = 0.0;
        }
        
               
        std::cout << "Case #" << i+1 << ": " << findDistance(rx, ry, rz) << " " << t << std::endl;
    }

    return 0;
}

