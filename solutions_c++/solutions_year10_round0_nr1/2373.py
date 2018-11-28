#include <iostream>
#include <vector>
#include <algorithm>

const int X = 0;
const int Y = 1;

template<class T>
    class V
{
public:
    V(int n = 0)
    {
        v.resize(n);
    }
    
    T & at(int i) 
    {
        return v.at(i);
    }
    
    const T & at(int i) const
    {
        return v.at(i);
    }
    
    void resize(int n) { v.resize(n); }
    int size() const { return v.size(); }
    
    void fill(const T & t) 
    {
        fill(v.begin(), v.end(), t);
    }
    
    void fill(int i, int j, const T & t)
    {
        fill(v.begin() + i, v.begin() + j, t);
    }
    
    
private:
    std::vector<T> v;
};

template<class T>
    std::istream & operator>> (std::istream & i, V<T> & v)
{
    int n;
    
    i >> n;
    
    v.resize(n);
    for (int j = 0; j < n; j++)
    {
        i >> v.at(j);
    }        
    
    return i;
}


template<class T>
    std::ostream & operator<< (std::ostream & o, const V<T> & v)
{
    o << v.size() << std::endl;
    
    for (int j = 0; j < v.size(); j++)
    {
        o << v.at(j) << " ";
    }   
    o << std::endl;
    return o;
}

template <class T>
    class M
{
public:
    M(int x = 0, int y = 0)
    {
        resize(x, y);
    }
    
    void resize(int x, int y)
    {
        n_cols = x;
        n_rows = y;
        m.resize(n_rows);
        for (int i = 0; i < y; ++i)
            m.at(i).resize(n_cols);        
    }
    
    V<int> size() const 
    { 
        V<int> v(2); v.at(0) = n_cols; v.at(1) = n_rows; 
        return v;
    }
    
    T & at(int x, int y)
    {
        return m.at(y).at(x);
    }

    const T & at(int x, int y) const
    {
        return m.at(y).at(x);
    }
    
    void fill(const T & t)
    {
        for (int i = 0; i < n_rows; ++i)
            m.at(i).fill(t);
    }

    void fill(int x1, int y1, int x2, int y2, const T & t)
    {
        for (int i = y1; i <= y2; ++i)
            m.at(i).fill(x1, x2, t);
    }

    
private:
    V<V<T> > m;
    int n_cols, n_rows;
};

template<class T>
    std::istream & operator>> (std::istream & i, M<T> & m)
{
    int x,y;
    
    i >> x >> y;
    
    m.resize(x, y);
    for (int k = 0; k < y; k++)
        for (int j = 0; j < x; j++)
        {
            i >> m.at(j,k);
        }        
    
    return i;
}


template<class T>
    std::ostream & operator<< (std::ostream & o, const M<T> & m)
{
    V<int> sz = m.size();
    o << sz.at(X) << " " << sz.at(Y) << std::endl;
    
    for (int k = 0; k < sz.at(Y); k++)
    {
        for (int j = 0; j < sz.at(X); j++)
        {
            o << m.at(j, k) << " ";
        }
        o << std::endl;
    }
    
    o << std::endl;
    return o;
}
