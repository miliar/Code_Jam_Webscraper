#include <iostream>
#include <string>
#include <vector>
#include <stdint.h>

/* STRATEGY

Find the sinks, give them the proper letter names, then go through the map
until everyone connects to a sink directly or indirectly.

to compile:

g++ ws.cpp

*/

typedef uint16_t alt_t;
typedef std::vector<alt_t> alt_vec_t;
typedef std::vector<alt_vec_t> alt_matrix_t;

typedef std::vector<char> char_vec_t;
typedef std::vector<char_vec_t> char_matrix_t;

void output(const char_matrix_t& output, size_t line)
{
    std::cout << "Case #" << line + 1 << ": " << std::endl;

    size_t width = output.size();
    size_t height = output[0].size();

    for (size_t y = 0; y < height; ++y)
    {
        for (size_t x = 0; x < width; ++x)
        {
            std::cout << output[x][y];
            if (x < (width - 1))
                std::cout << " ";
        }
        std::cout << std::endl;
    }

}

class Shedder
{
    private:
    const alt_matrix_t& m_alts;
    char_matrix_t m_sheds;
    size_t m_width;
    size_t m_height;

#ifdef UNIT_TEST
    public:
#endif
    static const char EMPTY = '$';

    public:
    Shedder(const alt_matrix_t& alt_matrix)
        : m_alts(alt_matrix),
          m_width(alt_matrix.size()),
          m_height(alt_matrix[0].size())
    {

        // resize sheds
        m_sheds.resize(m_width);
        for (size_t x = 0; x < m_width; ++x)
        {
            m_sheds[x].resize(m_height, EMPTY);
        }
    }

    void find_sinks()
    {
        char sink_char = 'a';

        for (size_t y = 0; y < m_height; ++y)
        {
            for (size_t x = 0; x < m_width; ++x)
            {
                if (is_sink(x, y))
                    m_sheds[x][y] = sink_char++;
            }
        }
    }

    bool is_sink(size_t x, size_t y)
    {
        return is_sink(m_alts[x][y], n_alt(x, y), e_alt(x, y), s_alt(x, y), w_alt(x, y));
    }

    bool is_sink(alt_t a, alt_t n, alt_t e, alt_t s, alt_t w)
    {
        return (a <= n && a <= e && a <= s && a <= w);
    }

    alt_t n_alt(size_t x, size_t y, alt_t max = 65535)
    {
        if (y == 0) return max;
        return m_alts[x][y-1];
    }

    alt_t s_alt(size_t x, size_t y, alt_t max = 65535)
    {
        if (y +1 >= m_height) return max;
        return m_alts[x][y+1];
    }

    alt_t w_alt(size_t x, size_t y, alt_t max = 65535)
    {
        if (x == 0) return max;
        return m_alts[x-1][y];
    }

    alt_t e_alt(size_t x, size_t y, alt_t max = 65535)
    {
        if (x + 1 >= m_width) return max;
        return m_alts[x+1][y];
    }

    void find_sheds()
    {
        while (has_empty())
        {
            for (size_t y = 0; y < m_height; ++y)
            {
                for (size_t x = 0; x < m_width; ++x)
                {
                    if (m_sheds[x][y] == EMPTY)
                    {
                        char shed = get_shed(x, y);
                        if (shed != EMPTY)
                            m_sheds[x][y] = shed;
                    }
                }
            }
        }

        fixup_sheds();
    }

    char get_shed(size_t x, size_t y)
    {
        return get_shed(n_alt(x, y), n_shed(x, y), e_alt(x, y), e_shed(x, y), s_alt(x, y), s_shed(x, y), w_alt(x, y), w_shed(x, y));
    }

    static char get_shed(alt_t n, char nc, alt_t e, char ec, alt_t s, char sc, alt_t w, char wc)
    {
        // order is n, w, e, s
        if (n <= w && n <= e && n <= s)
        {
            return nc;
        }
        else if (w < n && w <= e && w <= s)
        {
            return wc;
        }
        else if (e < n && e < w && e <= s)
        {
            return ec;
        }
        else if (s < n && s < w && s < e)
        {
            return sc;
        }
        assert(0 && "missed a case!");
    }

    char n_shed(size_t x, size_t y)
    {
        if (y == 0) return EMPTY;
        return m_sheds[x][y-1];
    }

    char s_shed(size_t x, size_t y)
    {
        if (y +1 >= m_height) return EMPTY;
        return m_sheds[x][y+1];
    }

    char w_shed(size_t x, size_t y)
    {
        if (x == 0) return EMPTY;
        return m_sheds[x-1][y];
    }

    char e_shed(size_t x, size_t y)
    {
        if (x + 1 >= m_width) return EMPTY;
        return m_sheds[x+1][y];
    }

    bool has_empty()
    {
        for (size_t y = 0; y < m_height; ++y)
        {
            for (size_t x = 0; x < m_width; ++x)
            {
                if (m_sheds[x][y] == EMPTY)
                    return true;
            }
        }

        return false;
    }

    void fixup_sheds()
    {
        // meet ordering constraints
        char max_shed = 'a';

        for (size_t y = 0; y < m_height; ++y)
        {
            for (size_t x = 0; x < m_width; ++x)
            {
                char shed = m_sheds[x][y];

                if (shed == EMPTY) 
                    continue; // only should happen while debugging

                if (shed < max_shed)
                    continue;
                
                if (shed == max_shed)
                {
                    // in the right place
                    ++max_shed;
                    continue;
                }

                if (shed > max_shed)
                {
                    swap_sheds(shed, max_shed++);
                }
            }
        }
    }

    void swap_sheds(char s1, char s2)
    {
        for (size_t y = 0; y < m_height; ++y)
        {
            for (size_t x = 0; x < m_width; ++x)
            {
                if (m_sheds[x][y] == s1)
                {
                    m_sheds[x][y] = s2;
                }
                else if (m_sheds[x][y] == s2)
                {
                    m_sheds[x][y] = s1;
                }
            }
        }
    }

    const char_matrix_t& get_shed_map()
    {
        return m_sheds;
    }
};

const char Shedder::EMPTY;

void do_watersheds(const alt_matrix_t& alt_matrix, size_t tcase)
{
    Shedder shedder(alt_matrix);
    shedder.find_sinks();
    shedder.find_sheds();
    output(shedder.get_shed_map(), tcase);
}

int main()
{
    size_t num_maps;
    std::cin >> num_maps;

#ifdef UNIT_TEST
// nwes
    assert(Shedder::get_shed(1, 'n', 1, 'e', 1, 's', 1, 'w') == 'n'); // N first
    assert(Shedder::get_shed(1, 'n', 1, 'e', 1, 's', 2, 'w') == 'n'); 
    assert(Shedder::get_shed(1, 'n', 1, 'e', 2, 's', 1, 'w') == 'n'); 
    assert(Shedder::get_shed(1, 'n', 2, 'e', 1, 's', 1, 'w') == 'n'); 

    assert(Shedder::get_shed(2, 'n', 1, 'e', 1, 's', 1, 'w') == 'w'); // W next
    assert(Shedder::get_shed(2, 'n', 2, 'e', 1, 's', 1, 'w') == 'w'); 
    assert(Shedder::get_shed(2, 'n', 1, 'e', 2, 's', 1, 'w') == 'w'); 

    assert(Shedder::get_shed(2, 'n', 1, 'e', 1, 's', 2, 'w') == 'e'); // E next

    assert(Shedder::get_shed(2, 'n', 2, 'e', 1, 's', 2, 'w') == 's'); // S next
#endif
    for (size_t i_map = 0; i_map < num_maps; ++i_map)
    {
        size_t height, width;
        std::cin >> height >> width;
        alt_matrix_t altitudes;

        // resize first (we want [x][y] but input is y, then x
        altitudes.resize(width);
        for (size_t x = 0; x < width; ++x)
        {
            altitudes[x].resize(height);
        }

        for (size_t y = 0; y < height; ++y)
        {
            for (size_t x = 0; x < width; ++x)
            {
                alt_t altitude;
                std::cin >> altitude;
                altitudes[x][y] = altitude;
                //std::cout << x << "," << y << ":" << altitude << std::endl;
            }
        }

        do_watersheds(altitudes, i_map);
    }

    return 0;
}
