import Data.Char (digitToInt)
import Control.Arrow

digitToList :: Integer -> [Integer]
digitToList = map (toInteger . digitToInt) . show

isPalindrome :: Eq a => [a] -> Bool
isPalindrome = (uncurry (==) . (id &&& reverse))

isSquareFair :: Integer -> Bool
isSquareFair x = isPalindrome (digitToList x) && isPalindrome (digitToList $ x^2)

findFairAndSquare :: Integer -> Integer -> [Integer]
findFairAndSquare a b = [x^2 | x <- [a..b], isSquareFair x]

main :: IO ()
main = putStrLn $ show $ findFairAndSquare 1 $ 10^7