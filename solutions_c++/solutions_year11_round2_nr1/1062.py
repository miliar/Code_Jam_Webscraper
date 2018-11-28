#include <list>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <string>
#include <math.h>
#include <algorithm>

struct schedule_t
{
   friend std::istream & operator >> (std::istream & stream, schedule_t & s)
   {
      stream >> s.teams_;
      s.results_.resize(s.teams_ * s.teams_);
      for (size_t l = 0; l != s.results_.size(); ++l)
      {
         char c;
         stream >> c;
         if (c == '.')
            s.results_[l] = 0;
         else if (c == '1')
            s.results_[l] = 1;
         else
            s.results_[l] = -1;
      }

      s.init_wps();

      return stream;
   }

   size_t teams() const { return teams_; }

   double rpi(size_t id) const
   {
      return wp_[id] * 0.25 + owp_[id] * 0.5 + oowp_[id] * 0.25;
   }

private:
   void init_wps()
   {
      wp_.resize(teams_);
      owp_.resize(teams_);
      oowp_.resize(teams_);

      for (size_t l = 0; l != teams_; ++l)
      {
         size_t f = 0, s = 0;
         for (size_t k = 0; k != teams_; ++k)
         {
            size_t r = results_[l * teams_ + k];

            if (r == 0)
               continue;

            s++;

            if (r == -1)
               continue;

            f++;
         }

         if (s != 0)
            wp_[l] = ((double)f) / s;
         else
            wp_[l] = 0;
      }

      for (size_t l = 0; l != teams_; ++l)
      {
         double wp = 0;
         size_t n = 0;
         for (size_t k = 0; k != teams_; ++k)
         {
            if (met(k, l))
            {
               wp += wpt(k, l);
               ++n;
            }
         }

         if (n != 0)
            wp /= n;

         owp_[l] = wp;
      }

      for (size_t l = 0; l != teams_; ++l)
      {
         double owp = 0;
         size_t n = 0;
         for (size_t k = 0; k != teams_; ++k)
         {
            if (met(k, l))
            {
               owp += owp_[k];
               ++n;
            }
         }

         if (n != 0)
            owp /= n;

         oowp_[l] = owp;
      }
   }

private:
   double wpt(size_t k, size_t l) const
   {
      size_t f = 0, s = 0;
      for (size_t t = 0; t != teams_; ++t)
      {
         if (t == l)
            continue;

         size_t id = results_[k * teams_ + t];

         if (id == 0)
            continue;

         ++s;

         if (id == -1)
            continue;

         ++f;
      }

      return ((double)f) / s;
   }

private:
   bool met(size_t k, size_t l) const
   {
      return results_[k * teams_ + l] != 0;
   }

private:
   size_t teams_;
   std::vector<int> results_;

   std::vector<double> wp_;
   std::vector<double> owp_;
   std::vector<double> oowp_;
};

int main()
{
   size_t T;
   std::cin >> T;

   for (size_t tc = 0; tc != T; ++tc)
   {
      schedule_t schedule;
      std::cin >> schedule;

      std::cout << "Case #" << tc + 1 << ":" << std::endl;

      for (size_t l = 0; l != schedule.teams(); ++l)
      {
         std::cout.precision(32);
         std::cout << schedule.rpi(l) << std::endl;
      }
   }
}