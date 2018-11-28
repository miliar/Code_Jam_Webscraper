#include <QTextStream>
#include <QVector>

#include <iostream>

using namespace std;

QMap<int, int> map_max_point_normal, map_max_point_surp;


int v_max(const QVector<int> & v)
{
    int r = v.at(0);
    
    Q_FOREACH(int i, v) 
        r = qMax(r, i);
            
    return r;
}

int v_min(const QVector<int> & v)
{
    int r = v.at(0);
    
    Q_FOREACH(int i, v) 
        r = qMin(r, i);
            
    return r;
}

int v_sum(const QVector<int> & v)
{ 
    int r = 0;
    
    Q_FOREACH(int i, v)
        r += i;
    
    return r;
}

void print_comb(QVector<int> & v, bool surp)
{
    Q_FOREACH(int i, v)
        cout << i << " ";
    
    if (surp) cout << "*";
    
    cout << "\n";
}


void generate_comb(int n, QVector<QVector<int> > & normal_comb, QVector<QVector<int> > & surp_comb)
{
    normal_comb.clear();
    surp_comb.clear();
    
    int i_start = qMax(0, n/3 - 2);
    int i_end = qMin(10, n/3 + 2);
                       
    QVector<int> c(3, i_start);
    bool done = false;
    
    int max_point_normal = 0;
    int max_point_surp = 0;
    
    do {
        int sum = v_sum(c);
        int min = v_min(c);
        int max = v_max(c);
        
        if (sum == n && (max - min <= 2)) {
            if (max - min <= 1) {
                normal_comb += c;
                // print_comb(c, false);
                max_point_normal = qMax(max_point_normal, max);
            }
            else {
                surp_comb += c;
                // print_comb(c, true);
                max_point_surp = qMax(max_point_surp, max);
            }
        }
        
        // next combination
        for (int i=0; i < 3;) {
            if (c.at(i) < i_end) {
                c[i]++;
                break;
            }
            else {
                c[i] = i_start;
                i++;
                done = i >= 3;
            }
        }
    } while (! done);
    
    map_max_point_normal[n] = max_point_normal;
    map_max_point_surp[n] = max_point_surp;
}

int solve(int N, int S, int p, QVector<int> & t)
{
    int r = 0;

    // Find how many combinations have no surprising points and pass the criteria
    Q_FOREACH(int i, t) {
        if (map_max_point_surp[i] == 0 && 
            map_max_point_normal[i] >= p)
            r++;
    }

    // Find how many combinations with surprising points always pass the criteria
    Q_FOREACH(int i, t) {
        if (map_max_point_surp[i] != 0 && 
            map_max_point_normal[i] >= p && 
            map_max_point_surp[i] >= p)
            r++;
    }
    
    int sometimes = 0;
    // Find how many combinations with surprising points pass criteria only with supr point but not with normal
    Q_FOREACH(int i, t) {
        if (map_max_point_surp[i] != 0 && 
            map_max_point_normal[i] < p && 
            map_max_point_surp[i] >= p)
            sometimes++;
    }
    
    r += qMin(S, sometimes);

    if (r > N) {
        cout << "Bug at line " << __LINE__ << "\n";
        exit(-1);
    }

    return r;
}

int main()
{
    QVector<QVector<int> > normal;
    QVector<QVector<int> > surp;
    
    // Generate combinations for all sums
    for (int i = 0; i <= 30; ++i) {
        // cout << "N = " << i << "\n";
        generate_comb(i, normal, surp);
        // cout << "-----------------------\n";
    }
    
    QTextStream qtin(stdin);
    
    int n_cases;
    
    qtin >> n_cases; qtin.readLine();
    
    for (int c = 1; c <= n_cases; ++c) {
        int N, S, p;
        QVector<int> t;
        
        qtin >> N >> S >> p;
        for (int i = 0; i < N; ++i) {
            int tmp;
            qtin >> tmp;
            t += tmp;
        }
        qtin.readLine();
        
        cout << "Case #" << c << ": " << solve(N, S, p, t) << "\n";
    }
}
